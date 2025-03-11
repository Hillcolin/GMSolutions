import torch
from PIL import Image, ImageDraw
import numpy as np
import os
import argparse

def load_model(weights_path, conf_thres=0.1):
    # Check if the weights file exists
    if not os.path.exists(weights_path):
        raise FileNotFoundError(f"Weights file not found: {weights_path}")
    
    # Load the YOLO model
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=weights_path, force_reload=True)
    model.eval()  # Set the model to evaluation mode
    model.conf = conf_thres  # Set confidence threshold
    return model

def preprocess_image(image_path, img_size=640):
    # Load and preprocess the image
    try:
        img = Image.open(image_path)
    except PermissionError:
        raise PermissionError(f"Permission denied: {image_path}")
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {image_path}")
    
    img = img.resize((img_size, img_size))
    img = np.array(img)
    img = img[:, :, ::-1].copy()  # Convert RGB to BGR
    return img

def run_inference(model, image):
    # Run inference on the image
    results = model(image)
    return results

def draw_bounding_boxes(image_path, results, model, output_path):
    # Load the image
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    # Get the bounding boxes and labels
    for *box, conf, cls in results.xyxy[0]:  # xyxy format
        x_min, y_min, x_max, y_max = box
        draw.rectangle([x_min, y_min, x_max, y_max], outline="red", width=2)
        draw.text((x_min, y_min), f"{model.names[int(cls)]} {conf:.2f}", fill="red")

    # Save the image with bounding boxes
    output_image_path = os.path.join(output_path, os.path.basename(image_path))
    img.save(output_image_path)
    print(f"Results saved to {output_image_path}")

def save_results(image_path, results, output_path):
    # Save detection details to results.txt
    results_file = os.path.join(output_path, 'results.txt')
    with open(results_file, 'a') as f:  # Open in append mode
        for *box, conf, cls in results.xyxy[0]:  # xyxy format
            x_min, y_min, x_max, y_max = box
            f.write(f"{os.path.basename(image_path)} {int(cls)} {conf:.2f} {x_min:.2f} {y_min:.2f} {x_max:.2f} {y_max:.2f}\n")
    print(f"Detection details saved to {results_file}")

def process_image(image_path, model, output_path):
    # Preprocess the image
    image = preprocess_image(image_path)

    # Run inference
    results = run_inference(model, image)

    # Debugging: Print the number of detections
    num_detections = len(results.xyxy[0])
    print(f"Number of detections for {image_path}: {num_detections}")

    if num_detections > 0:
        # Draw bounding boxes on the image and save it
        draw_bounding_boxes(image_path, results, model, output_path)

        # Save detection details to results.txt
        save_results(image_path, results, output_path)
    else:
        print(f"No detections for {image_path}")

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Parking Space Detection")
    parser.add_argument('--input', type=str, required=True, help="Path to the input image or directory")
    parser.add_argument('--output', type=str, required=True, help="Path to the output directory")
    parser.add_argument('--conf_thres', type=float, default=0.1, help="Confidence threshold for detections")
    args = parser.parse_args()

    # Paths
    weights_path = r'yolov5\runs\train\exp2\weights\best.pt'  # Use raw string to handle backslashes
    input_path = args.input
    output_path = args.output
    conf_thres = args.conf_thres

    # Ensure the output directory exists
    os.makedirs(output_path, exist_ok=True)

    # Load the model
    model = load_model(weights_path, conf_thres)

    # Check if the input path is a file or a directory
    if os.path.isdir(input_path):
        # Process all images in the directory
        for filename in os.listdir(input_path):
            image_path = os.path.join(input_path, filename)
            if os.path.isfile(image_path):
                process_image(image_path, model, output_path)
    else:
        # Process a single image
        process_image(input_path, model, output_path)

if __name__ == "__main__":
    main()
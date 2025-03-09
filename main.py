from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import os
from website import create_app, socketio

app = create_app()

# Allowed extensions for image uploads
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('basetemp.html')

@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify(success=False, message='No file part')
    file = request.files['image']
    if file.filename == '':
        return jsonify(success=False, message='No selected file')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.static_folder, filename)
        file.save(file_path)

        # Process the image using the AI algorithm
        processed_image_path = process_image(file_path)

        if processed_image_path:
            image_url = url_for('static', filename=os.path.basename(processed_image_path))
            socketio.emit('update_image', {'image_url': image_url})
            return jsonify(success=True, image_url=image_url)
        else:
            return jsonify(success=False, message='AI processing did not produce an output')
    return jsonify(success=False, message='File not allowed')

def process_image(file_path):
    # Placeholder for AI algorithm processing
    # Replace this with the actual processing code
    # Return the path to the processed image or None if processing fails
    processed_image_path = file_path  # For now, just return the original file path
    return processed_image_path

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
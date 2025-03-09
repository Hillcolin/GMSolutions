from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_socketio import emit
from . import socketio
import os
from pathlib import Path

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'admin' and password == '123':
            return redirect(url_for('views.image_page'))
        else:
            flash('Invalid credentials, please try again.', 'danger')
    
    return render_template('login.html')

@views.route('/image')
def image_page():
    return render_template('image.html')

@views.route('/process_image', methods=['POST'])
def process_image():
    # Assuming the YOLOv5 script saves the processed image to 'static/processed_image.jpg'
    from AI.yolov5 import run_yolo  # Import your YOLOv5 processing function
    input_image_path = request.form.get('input_image_path')
    output_image_path = os.path.join('static', 'processed_image.jpg')
    
    # Run YOLOv5 processing
    run_yolo(input_image_path, output_image_path)
    
    # Emit the update to the frontend
    image_url = url_for('static', filename='processed_image.jpg')
    socketio.emit('update_image', {'image_url': image_url}, broadcast=True)
    
    return 'Image processed', 200

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('new_image')
def handle_new_image(data):
    image_url = data['image_url']
    emit('update_image', {'image_url': image_url}, broadcast=True)

def update_image(image_url):
    socketio.emit('update_image', {'image_url': image_url})


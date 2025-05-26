from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from werkzeug.utils import secure_filename
from modules import enhance, edge_detection, sample_images

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enhance', methods=['GET', 'POST'])
def enhance_image():
    return enhance.handle_enhancement(app)

@app.route('/detect', methods=['GET', 'POST'])
def detect_edges():
    return edge_detection.handle_edge_detection(app)

@app.route('/samples')
def show_samples():
    return sample_images.display_samples()

if __name__ == '__main__':
    app.run(debug=True)

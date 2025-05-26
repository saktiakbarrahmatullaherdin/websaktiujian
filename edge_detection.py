import cv2
import numpy as np
import os
from flask import request, render_template
from werkzeug.utils import secure_filename

def detect_edges(img, method):
    if method == 'canny':
        return cv2.Canny(img, 100, 200)
    elif method == 'sobel':
        sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
        sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)
        return cv2.convertScaleAbs(sobelx + sobely)
    elif method == 'laplacian':
        return cv2.Laplacian(img, cv2.CV_64F)
    return img

def handle_edge_detection(app):
    if request.method == 'POST':
        file = request.files['image']
        method = request.form.get('method')
        if file and method:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
            edges = detect_edges(image, method)
            processed_path = os.path.join(app.config['UPLOAD_FOLDER'], f'{method}_{filename}')
            cv2.imwrite(processed_path, edges)

            return render_template('detect_edges.html', original=filename, processed=f'{method}_{filename}')
    return render_template('detect_edges.html')

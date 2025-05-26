import cv2
import numpy as np
import os
from flask import request, render_template
from werkzeug.utils import secure_filename

def enhance_image(img):
    return cv2.detailEnhance(img, sigma_s=10, sigma_r=0.15)

def handle_enhancement(app):
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            image = cv2.imread(filepath)
            enhanced = enhance_image(image)
            enhanced_path = os.path.join(app.config['UPLOAD_FOLDER'], 'enhanced_' + filename)
            cv2.imwrite(enhanced_path, enhanced)

            return render_template('enhance.html', original=filename, processed='enhanced_' + filename)
    return render_template('enhance.html')

from flask import render_template

def display_samples():
    sample_files = [
        'canny_sample.jpg',
        'sobel_sample.jpg',
        'laplacian_sample.jpg'
    ]
    return render_template('samples.html', samples=sample_files)

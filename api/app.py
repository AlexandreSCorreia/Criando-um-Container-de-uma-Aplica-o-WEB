from flask import Flask, request, jsonify, send_from_directory, url_for
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
CORS(app)

app.config['STATIC_IMAGES'] = 'static/images'

if not os.path.exists(app.config['STATIC_IMAGES']):
    os.makedirs(app.config['STATIC_IMAGES'])

@app.route('/images/<filename>')
def get_image(filename):
    return url_for('static', filename=f'images/{filename}')


@app.route('/images')
@cross_origin()
def get_images():
    image_dir = 'static/images'
    image_urls = []

    for filename in os.listdir(image_dir):
        print(filename)
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            url = url_for('static', filename=f'images/{filename}')
            image_urls.append(url)
    return jsonify(image_urls)

@app.route('/')
def index():
    return "Hello, World!"
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
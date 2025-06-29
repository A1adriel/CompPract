from flask import Flask, request, jsonify, send_from_directory
from PIL import Image
import io
import os


app = Flask(__name__)

# Serve HTML form
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/login')
def login():
    return {"author": "1150432"}


@app.route('/size2json', methods=['GET', 'POST'])
def size2json():
    if 'image' not in request.files:
        return jsonify({"result": "no file provided"}), 400

    file = request.files['image']

    if not file.filename.lower().endswith('.png'):
        return jsonify({"result": "invalid filetype"}), 400

    try:
        img = Image.open(io.BytesIO(file.read()))
        return jsonify({"width": img.width, "height": img.height})
    except:
        return jsonify({"result": "invalid image"}), 400


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
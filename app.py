import os
import logging
import tempfile
from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "uploads"

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=400):
        Exception.__init__(self)
        self.error_message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return {
            'message': self.error_message,
            'error': True,
        }

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    return error.to_dict(), error.status_code

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/upload', methods=['POST'])
def upload():
    try:
        logging.info(request.files)
        uploaded_file = request.files['image']
    except:
        raise InvalidUsage("Please provide image to upload", status_code=400)

    if uploaded_file.content_type != 'image/jpeg':
        raise InvalidUsage("Only JPEG images are allowed", status_code=400)

    try:
        filename = secure_filename(uploaded_file.filename)
        destination_file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        uploaded_file.save(destination_file)
        return {"file": filename}, 201
    except:
        raise
        raise InvalidUsage('Failed to upload image', status_code=500)
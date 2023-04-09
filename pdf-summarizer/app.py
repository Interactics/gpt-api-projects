import os
import base64
from io import BytesIO
from PyPDF2 import PdfReader
import requests
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
import pathlib
import openai
import os

UPLOAD_FOLDER = 'temp'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

env_path = pathlib.Path('..') / '.env'
load_dotenv(dotenv_path=env_path)
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__, static_folder='public')
CORS(app)

# Add these missing configurations
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100 MB
app.config['UPLOAD_FOLDER'] = 'temp'

# Add the allowed_file function
ALLOWED_EXTENSIONS = {'pdf'}

language_mapping = {
    'en': 'English',
    'ko': 'Korean',
    'es': 'Spanish',
    'fr': 'French',
    # Add more languages as needed
}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Add the missing extract_text_from_pdf function
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as fr:
        reader = PdfReader(fr)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

@app.route('/upload', methods=['POST'])
def upload():
    language = request.form.get('language', 'english')  # Add this line

    if 'pdf' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['pdf']

    if file.filename == '':
        return jsonify({"error": "No file provided"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            try:
                text = extract_text_from_pdf(filepath)
            except Exception as e:
                return jsonify({"error": f"Error extracting text from PDF: {str(e)}"}), 500

            try:
                summary = get_summary(text, language)
            except Exception as e:
                return jsonify({"error": f"Error generating summary: {str(e)}"}), 500

            return jsonify({"summary": summary}), 200
        finally:
            os.remove(filepath)

    return jsonify({"error": "Invalid file type"}), 400

def get_summary(text, language):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": f"You are an AI that can summarize text efficiently in {language}."
            },
            {
                "role": "user",
                "content": f"Summarize the following text: {text}"
            }
        ],
    )

    if response['choices'] and response['choices'][0]['message']:
        return response['choices'][0]['message']['content']
    else:
        raise Exception('Error while getting summary')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join('public', path)):
        return send_from_directory('public', path)
    else:
        return send_from_directory('public', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)

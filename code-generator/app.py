import openai
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import pathlib
import re

# Load environment variables from .env file

env_path = pathlib.Path('..') / '.env'
load_dotenv(dotenv_path=env_path)
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

# Set up the OpenAI API key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_code():
    req = request.get_json()
    description = req['description']
    language = req['language']

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": f"Generate {language} code snippets based on user descriptions."
            },
            {
                "role": "user",
                "content": f"Write a {language} code snippet that {description}"
            }
        ],
    )

    generated_text = response['choices'][0]['message']['content']
    code_pattern = re.compile(r'```(?:[\w\s]+)?\n(.*?)```', re.DOTALL)
    code_match = code_pattern.search(generated_text)

    if code_match:
        generated_code = code_match.group(1).strip()
    else:
        generated_code = "Failed to extract code snippet. Please try again."

    file_extension = language.lower()
    if file_extension == "python":
        file_extension = "py"
    elif file_extension == "javascript":
        file_extension = "js"
    elif file_extension == "c++":
        file_extension = "cpp"
    # Add more languages and their file extensions here

    return jsonify({"code": generated_code, "file_extension": file_extension})
if __name__ == '__main__':
    app.run(debug=True)

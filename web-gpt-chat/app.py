from flask import Flask, render_template, request, jsonify
import requests
import json
import openai
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/api/generate-response', methods=['POST'])
def generate_response():
    data = request.get_json()
    message = data.get('message')

    if not message:
        return jsonify({'response': 'No message provided'}), 400

    try:
        prompt = f"User: {message}\nAI:"
        response= openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "chatgpt3.5"
                },
                {
                    "role": "user",
                    "content": message
                }
            ],
        )

        generated_text = response.choices[0].message.content
        return jsonify({'response': generated_text})
    except Exception as e:
        print(e)
        return jsonify({'response': 'Error generating response'}), 500


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)



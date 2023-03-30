from flask import Flask, render_template, request, redirect, url_for
import re
import requests
from bs4 import BeautifulSoup
import openai
import os
from dotenv import load_dotenv
import pathlib

app = Flask(__name__)

env_path = pathlib.Path('..') / '.env'
load_dotenv(dotenv_path=env_path)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = ' '.join([p.get_text() for p in soup.find_all('p')])
    return content

def split_text(text, max_tokens):
    tokens = text.split(' ')
    chunks = []
    current_chunk = []

    for token in tokens:
        if len(' '.join(current_chunk + [token])) <= max_tokens:
            current_chunk.append(token)
        else:
            chunks.append(' '.join(current_chunk))
            current_chunk = [token]

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks

def generate_summary(content):
    max_tokens = 4097 - 100  # 여유 공간을 남겨둡니다.
    chunks = split_text(content, max_tokens)

    summarized_chunks = []

    for chunk in chunks:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "chatgpt3.5"
                },
                {
                    "role": "user",
                    "content": f"summarize the following content:\n\n{chunk}\n"
                }
            ],
        )

        summary = response.choices[0].message['content'].strip()
        summarized_chunks.append(summary)

    final_summary = ' '.join(summarized_chunks)
    return final_summary

def format_summary(summary):
    # 문장 경계를 찾아 문장을 나눕니다.
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', summary)

    # 문장들을 문단으로 나누어 줍니다.
    formatted_summary = "\n".join([" ".join(sentences[i:i + 3]) for i in range(0, len(sentences), 3)])

    return formatted_summary

@app.route('/summarize', methods=['POST'])
def summarize():
    url = request.form['url']
    content = fetch_content(url)
    summary = generate_summary(content)
    formatted_summary = format_summary(summary)
    return render_template('result.html', summary=formatted_summary)


if __name__ == '__main__':
    app.run(debug=True)

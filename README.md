# GPT API Projects

This repository contains various projects utilizing the OpenAI GPT API.

## Projects

<<<<<<< HEAD
Code Generator with GPT-3.5 API
This is a web application that generates code files using the GPT-3.5 API from OpenAI. Users can input their code requirements and desired programming language, and the application generates a code snippet based on the input.

Web GPT Chat
This is a web application that allows users to chat with a large language model trained by OpenAI, based on the GPT-3.5 architecture. Users can input their message, and the model responds with a generated message.

Webpage Summarizer
This is a web application that summarizes a given web page using the BeautifulSoup library in Python. Users can input a URL, and the application generates a summary of the page.

Please see the individual README files for each project for more information on how to set up and use each application.
=======
### 1. Web GPT Chat
>>>>>>> 4529e69fe2bb803203060ddd053a6e70e4b835ee

This is a simple web chat application built with Flask and OpenAI's GPT-3.5 model.

#### Features

- Allows users to send messages to an OpenAI-powered chatbot
- Displays chat history between the user and the chatbot
- Shows typing indicator while waiting for a response from the chatbot
- Allows users to hide and show the chat window

#### Getting Started

To use this application, you'll need to set up an OpenAI API key. You can sign up for an API key at OpenAI's website. Once you have an API key, create a new file called `.env` in the root directory of the project and add your API key like this:

```
OPENAI_API_KEY=your-api-key-here
```


Next, install the required Python packages by running the following command:

```
pip install -r requirements.txt
```


Finally, start the Flask development server by running:
```
flask run
```


You should now be able to access the application by visiting http://localhost:5000 in your web browser.

#### Contributing

If you'd like to contribute to this project, please fork the repository and create a pull request with your changes.

#### License

This project is licensed under the MIT License. See the LICENSE file for details.

### 2. Webpage Summarizer

A web application that uses GPT-3.5 to generate summaries of web pages.

#### Getting Started

Follow the same instructions for setting up the OpenAI API key, installing the required packages, and starting the Flask development server as described in the Web GPT Chat section.

You should be able to access the Webpage Summarizer application by visiting http://localhost:5000 in your web browser.

#### Contributing

If you'd like to contribute to this project, please fork the repository and create a pull request with your changes.

#### License

This project is licensed under the MIT License. See the LICENSE file for details.

## License

This repository is licensed under the MIT License. See the LICENSE file for details.



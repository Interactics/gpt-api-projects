# GPT-API-Projects

This repository contains a collection of projects that utilize the OpenAI GPT API to perform various tasks. Each project in this repository demonstrates a different use case for the GPT API.

## Projects

### Code Generator with GPT-3.5 API
This is a web application that generates code files using the GPT-3.5 API from OpenAI. Users can input their code requirements and desired programming language, and the application generates a code snippet based on the input.

### Web GPT Chat
This is a web application that allows users to chat with a large language model trained by OpenAI, based on the GPT-3.5 architecture. Users can input their message, and the model responds with a generated message.

### Webpage Summarizer
This is a web application that summarizes a given web page using the BeautifulSoup library in Python. Users can input a URL, and the application generates a summary of the page.

Please see the individual README files for each project for more information on how to set up and use each application.


## Setup

1. Clone this repository:

```
git clone https://github.com/Interactics/gpt-api-projects.git
```

2. Install the required packages:
```
pip install -r requirements.txt
```

3. Set up a .env file in the root directory of the repository with the following content:

```
OPENAI_API_KEY=your_openai_api_key
```
Replace your `_openai_api_key` with your actual OpenAI API key.

## Running the projects

To run a specific project, navigate to the project's directory and execute its main script.

For example, to run the Website Content Summarizer project:

```
cd website_content_summarizer
python app.py
```

This will launch the Flask web application on your local machine. Open your web browser and navigate to http://localhost:5000 to access the application.

## Contributing

Contributions to this repository are welcome! If you have an idea for a new project or an improvement to an existing one, please feel free to submit a pull request or open an issue.

## License

This repository is licensed under the MIT License. See LICENSE for more information.

# GPT-API-Projects

This repository contains a collection of projects that utilize the OpenAI GPT API to perform various tasks. Each project in this repository demonstrates a different use case for the GPT API.

## Projects

1. __Website Content Summarizer__: This project is a Flask web application that takes a URL as input and returns a summarized version of the content found on the page. It uses the GPT-3.5-turbo model to generate the summaries.


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

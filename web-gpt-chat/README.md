# GPT Web

This is a simple web chat application built with Flask and OpenAI's GPT-3.5 model.

## Features

- Allows users to send messages to an OpenAI-powered chatbot
- Displays chat history between the user and the chatbot
- Shows typing indicator while waiting for a response from the chatbot
- Allows users to hide and show the chat window

## Getting Started

To use this application, you'll need to set up an OpenAI API key. 
You can sign up for an API key at [OpenAI's website](https://beta.openai.com/signup/). 
Once you have an API key, create a new file called `.env` in the root directory of the project and add your API key like this:

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

## Contributing

If you'd like to contribute to this project, please fork the repository and create a pull request with your changes.

## License



This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


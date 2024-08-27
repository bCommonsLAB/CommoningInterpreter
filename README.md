# Commonin Interpreter README





## Introduction

Welcome to your Commoning Interpreter project! This application is a German/Italian Speech-to-Text Bot with translation and summarization functions. This guide explains step-by-step how to start your Python server and ensure that all files are in the same directory.

## Prerequisites

- Python must be installed on your system. You can download and install Python from the [official website](https://www.python.org/).
- The package manager `pip` should also be installed to install the necessary packages.

## Installation

Before starting the server, some Python packages need to be installed. Open a terminal or command prompt and run the following commands:

```bash
pip install Flask Flask-CORS openai
```

These commands install the following packages:
- `Flask`: A lightweight WSGI Web Application Framework.
- `Flask-CORS`: An extension for Flask that supports Cross-Origin Resource Sharing (CORS).
- `openai`: A Python library for the OpenAI API.

## Project Structure

Ensure that all files are in the same directory. Your project structure should look like this:

```
/your-project-directory
    ├── .gitignore
    ├── README.md
    ├── app.py
    ├── background.js
    ├── config.py
    ├── index.html
    ├── loader.css
    ├── recorder.js
    └── styles.css
    
```

## Configuration File `config.py`

Open the configuration file named `config.py` and add your OpenAI API key there. It should look like this at the beginning:

```python
myopenkey = 'put your api key here'
```

## Starting the Server

To start the server, open a terminal or command prompt in the directory where your `app.py` is located and run the following command:

```bash
python app.py
```

Your server should now be running and accessible at `http://localhost:5000`.

## Using the Application

Open the `index.html` file in your browser to use the speech-to-text functionality as well as the translation and summarization features. Additional functions and instructions can be found in the relevant JavaScript files (`background.js` and `recorder.js`) and the `styles.css` file for styling.

## Contact and Support

If you have any questions or issues, feel free to contact us. For more information on this and other projects, check here: https://www.bcommonslab.org/

If you want to try out the application, feel free to do so here: 
[Commoning Interpreter](https://www.bcommonslab.org/en/visions/commoningversteher)

Good luck and enjoy your Commoning Interpreter project!

#!/usr/bin/env python
"""
A simple Flask application.
"""

from flask import Flask, request, render_template

# Initialize Flask App
APP = Flask(__name__, template_folder='templates')


@APP.route('/')
def home():
    """
    Render the home page.
    """
    return render_template('index.html')


@APP.route('/hello', methods=['POST'])
def hello():
    """
    Handle form submission and display a greeting message.
    """
    inputs = [x for x in request.form.values()]
    result = f"Hello There {inputs[0]}"  # Using f-string for readability
    return render_template('index.html', hello_text=result)


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)  # Enable debugging for development

#!/usr/bin/env python3
"""
This is a simple Flask app that displays a welcome message.
"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """
    Displays the welcome message on the homepage.
    """

    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)

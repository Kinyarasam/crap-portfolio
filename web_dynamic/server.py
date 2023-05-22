#!/usr/bin/env python3
"""Starts a Flask Web Application
"""
import os
import uuid
import dotenv
from flask import Flask, render_template


dotenv.load_dotenv() # take enviroment variables from .env.


app = Flask(__name__)
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')


@app.route('/', strict_slashes=False)
def index():
    """Home Route
    """
    cache_id = uuid.uuid4()
    return render_template('index.html',
                           cache_id=cache_id)


if __name__ == '__main__':
    """Main
    """
    app.run(host=HOST, port=PORT)

#!/usr/bin/python3
"""flask model for route"""
from flask import Flask
app = Flask(__name__)



@app.route('/', strict_slashes=False)
def hello_hbnb():
    """hbnb route page"""
    return 'Hello HBNB!'

@app.route('/', strict_slashes=False)
def hbnb():
    return 'HBNB'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
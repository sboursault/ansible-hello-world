#!/usr/bin/env python

from flask import Flask
import os

host=os.getenv('HELLO_WORLD_HOST', 'unknown')

app = Flask(__name__)

@app.route('/info')
def info():
    return 'host: ' + host + '; version: 1.1\n'

@app.route('/')
def hello():
    return "Hello World!\n"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!\n".format(name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)

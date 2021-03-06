#!/usr/bin/env python

from flask import Flask
import socket

host_name=socket.gethostname()


app = Flask(__name__)

@app.route('/info')
def info():
    return 'host: ' + host_name + '; version: 1.0\n'

@app.route('/')
def hello():
    return "Hello World!\n"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)


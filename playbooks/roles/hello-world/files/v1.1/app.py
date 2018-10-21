from flask import Flask
import os

port=os.getenv('HELLO_WORLD_PORT', 5000)
host=os.getenv('HELLO_WORLD_HOST', 'unknown')

app = Flask(__name__)

@app.route('/info')
def info():
    return 'host: ' + host + '; version: 1.1'

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)



sudo apt-get -y install python-pip
sudo pip install Flask

app.py
-----------------------
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True, port=5001)
    
-----------------------
    
python app.py


curl -i http://127.0.0.1:5000/

# KILL PROCESS
kill `ps aux | grep -F 'app.py' | grep -v -F 'grep' | awk '{ print $2 }'`
        
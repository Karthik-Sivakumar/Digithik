from flask import Flask
import os

port = os.environ.get('PORT')

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run('0.0.0.0',port)

from flask import Flask
import os

port = os.environ.get('PORT')

app = Flask(__name__)

@app.route("/")
def hello():
    app.run('0.0.0.0',port)    

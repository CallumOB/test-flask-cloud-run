from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello anew from Dockerised Flask"

@app.route("/route32a")
def route32a():
    return "Hello from the 32A"

@app.route("/route")
def route():
    number=request.args.get('number')
    return "Hello from the {}".format(number)

@app.route("/lab5")
def lab5(): 
    return "Hello from Google Cloud Build for lab 5!"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')

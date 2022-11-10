#Import libraries and packages
from flask import flask
#create our application
app = Flask(__name__)

#Create a directory
@app.route('/')
def home():
    return "Hello world"

@app.route('/<name>')
def home2(name):
    return "Hello"+ name

#start our application
if __name__=="__main__":
    app.run(

    )
    
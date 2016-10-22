#---- Flask Hello World ----#

#import flask class
from flask import Flask

#create application object
app = Flask(__name__)

#use decorators to link the function to a url

@app.route("/")
@app.route("/hello")

#define the view using a function, wich returns a string
def hello_world():
	return "Hello, World!"

#start the development server using the run() method
if __name__ == "__main__":
	app.run()

	

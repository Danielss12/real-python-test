#---- Flask Hello World ----#

#import flask class
from flask import Flask

#create application object
app = Flask(__name__)

#error handling
app.config["DEBUG"] = True


#use decorators to link the function to a url



@app.route("/integer/<int:value>")
#define the view using a function, wich returns a string
def int_type(value):
	print value + 1
	return "correct"
	

@app.route("/test/<search_query>")
def search(search_query):
	return search_query

@app.route("/name/<name>")
def index(name):
	if name.lower() == "michael":
		return "Hello!?!?!?!, {}".format(name), 200
	else:
	    return "Not Found", 404	
#start the development server using the run() method
if __name__ == "__main__":
	app.run()



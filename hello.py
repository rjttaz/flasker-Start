from flask import Flask, render_template


#Create a Flask Instence
app = Flask(__name__)

#Create a route decorator
@app.route('/')

def index():
	first_name="John"
	return render_template("index.html")
#	return "<h1>Hello World!</h1>"

#localhost:5000/user/Rod
@app.route('/user/<name>')

def User(name):
	return render_template("user.html", user_name=name )

	# Create Custom Error Pages

	# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"),404

	# Internal Server Error URL
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"),500
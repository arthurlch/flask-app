###
"""

Application using the python framework ' Flask '
Flask official website: https://palletsprojects.com/p/flask/
Flask documentation: http://flask.palletsprojects.com/en/1.1.x/

Features: 
Login/Logout
Post message
Blog type
User management
User Registration



"""
###


from flask import Flask, url_for, render_template
# import flask framework 
# import url_for (avoid hard coding of the urls)
# define name app app = __name__
app = Flask(__name__)

# .route decorator 
# define the route of the pageORurl (routing)
# .route decorator bind function to an url
# root https://myapp.com/  root 
# Other routes will be be for example https://myapp.com/user-profil
@app.route('/')
# 1 function with two routes / & /home
@app.route('/home')
# Function which do the rendering 
# return a template 
# templates are html templates and are located in flask_app/templates/ 
def home():
	return render_template('home.html')

# About page
# def(about) route /about
@app.route('/about')
def about():
	return ''


# user section 
@app.route('/user/<username>')
# def username 	profil funct
def profile(username):
	# show user profil 
	return "{}'s profile".format(username)

# Login d
# def login route & associated func 
# login  hashing & sec 

@app.route('/login')
def login_func():
	return ' Attempting to login?'


"""/
/login
/login?next=/
/user/john%Doe
"""

#login
@app.route('/login')
def login():
	return 'login'



# users post sectin 
# converter int: post_id = integers 
# converters "string:,int:,float:,path:"
@app.route('/post/<int:post_id>')
# def user post_id func 
def show_post(post_id):
	return 'Post %d' % post_id 


# python idiom __name_ = '__main__' 
# open file using the terminal ' python3 app.py'
# Terminal run flask OFF 
if __name__ == '__main__':
	app.run(debug=True)	




 	









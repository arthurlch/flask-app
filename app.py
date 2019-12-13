###
"""

Application using the python framework ' Flask '
Flask official website: https://palletsprojects.com/p/flask/
Flask documentation: http://flask.palletsprojects.com/en/1.1.x/

This application is a sample to my study about Back-end and python framework and will serve the basic feautures of a modern app.

Feel free to use this projects for whatever purposes. 


Features  of the app: 
Login/Logout
Post message
Blog type / User input 
User management
User Registration


"""
###

from flask import Flask, url_for, render_template
# import flask framework 
# import url_for (avoid hard coding of the urls)
# define name app app = __name__
app = Flask(__name__)




# .route decorator for home define home page + render template of home 
@app.route("/")
@app.route("/home") 
def home():
	return render_template('home.html', posts=posts)
# dummy data 
# the dummy data will serve to show how to transfer data from app.py ( flask to templates made in html)
posts = [
		{
			'author':'Author',
			'title':'post title',
			'content':'First post of content',
			'date_posted':'April 20, 2018'


		},

		{
			'author':'Author',
			'title':'post title',
			'content':'First post of content',
			'date_posted':'April 20, 2018'

		}
		]

# def about page route + render 
@app.route('/about')
def about():
	return render_template('about.html', about_profil=about_profil, title='About')

about_profil = [{
	'user':'name'
}]


@app.route('/register')
def register_user():
	return render_template('register_user.html')

@app.route('/login')
def login():	
	return render_template('login')

@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)
name = [{
	'name':'name'
}]

# python idiom __name_ = '__main__' 
# open file using the terminal ' python3 app.py'
# Terminal run flask OFF 
if __name__ == '__main__':
	app.run(debug=True)	




 	









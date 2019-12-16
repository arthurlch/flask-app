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

from flask import Flask, url_for, render_template, flash, redirect
# import flask framework 
# import url_for (avoid hard coding of the urls)
from forms import RegistrationForm, LoginForm
# python idiom = __name__
app = Flask(__name__)
# secret key  16 Characters 16bit key / if public make new
app.config['SECRET_KEY'] ='b88b9d2380bfe69dbb922efa674210a5'


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


@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)
name = [{
	'name':'name'
}]

""" Register part route/form/class/return string & redirect user """
# HTML methods  GET to transfer retrieve the data from the form, POST send the data retrieved with GET() to the database 
@app.route('/register', methods=['GET', 'POST']) 
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		# f string to convert input to string for greeting message ' Account created for {} '
		flash(f' Account created for {form.username.data}', 'success') #layout.html line 71 display a message when successfully logged
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST']) # https request to retrieve and send data to the database
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == "admin@blog.com" and form.password.data == "password": # dummy data to fake login
			flash('You have been logged-in', 'success')
			return redirect(url_for('home'))
		else:
			flash(' Unsuccessful temptative', 'danger')
	return render_template('login.html', title='Login', form=form)

# python idiom __name_ = '__main__' 
# open file using the terminal ' python3 app.py'
# Terminal run flask OFF 
if __name__ == '__main__':
	app.run(debug=True)	




 	









from flask import url_for, render_template, flash, redirect
from application import app
from application.forms import RegistrationForm, LoginForm
from application.models import User,Post



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

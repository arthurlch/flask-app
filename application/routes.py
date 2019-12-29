from flask import url_for, render_template, flash, redirect, request
from application import app, db, bcrypt
from application.forms import RegistrationForm, LoginForm
from application.models import User,Post
from flask_login import login_user, current_user, logout_user, login_required


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
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		# create user. user = mail, username, hashed password from form.data 
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		# add the user in the data base and commit the change to the database
		db.session.add(user)
		db.session.commit()
		# f string to convert input to string for greeting message ' Account created for {} '
		flash('Your account has been created! You can now Log In', 'success') #layout.html line 71 display a message when successfully logged
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST']) # https request to retrieve and send data to the database
def login():
	""" login form and submit. if email of user is = email in database then pick first    """
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user  and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next') # args dict: https://www.geeksforgeeks.org/args-kwargs-python/
			return redirect(next_page) if next_page else redirect(url_for('home')) # redirect to next page if next page exist(account)	
		else:
			flash(' Unsuccessful temptative', 'danger')
	return render_template('login.html', title='Login', form=form)
# return logout input to home page 
@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))
# render account page
@app.route('/account')	
@login_required
def account():
	""" define user account  """
	image_file = url_for('static', filename='profile_pics/' + current_user.image_file) # path for user profile picture
	return render_template('account.html', title='Account') # render account.html file


from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import User


"""import flask_wtf: https://flask-wtf.readthedocs.io/en/stable/ 
	import stringfield for displaying a field
	import .validators to include validators as dataRequired(input required from the user),
	Lenght to set a min and max lenght of the Username of the user"""


"""Define the registration form, define a stringfield with an input(Datarequired), and a min-max lenght of the username"""
class RegistrationForm(FlaskForm):

	username = StringField('Username ', 
									validators=[DataRequired(), Length(min=2, max=15)])
	email = StringField('Email ', 
									validators=[DataRequired(), Email()])
	password = PasswordField('Password ', 
									validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password ', 
									validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')
	### validate fields from forms, if username = usernam from data(db) then username taken, show message ###
	""" check if email already exist in the database """
	def validate_email(self, email):
		if email.data != current_user.email:
			user = User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('Adress Email already taken! Have you forgot your password?')

	""" check if the username exist already in the database """	
	def validate_username(self, username):
		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('Username taken, Please choose a different username')

""" class for the login form, we re-use the same code as above, define each Field """
class LoginForm(FlaskForm):
	
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

"""update the information of the user account"""
class RegistrationForm(FlaskForm):

	username = StringField('Username ', 
									validators=[DataRequired(), Length(min=2, max=15)])
	email = StringField('Email ', 
									validators=[DataRequired(), Email()])
	
	submit = SubmitField('Update')
	### validate fields from forms, if username = usernam from data(db) then username taken, show message ###
	""" check if email already exist in the database """
	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Adress Email already taken! Have you forgot your password?')

	""" check if the username exist already in the database """
	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('Username taken, Please choose a different username')
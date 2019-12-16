from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

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

""" class for the login form, we reused the same code as above """
class LoginForm(FlaskForm):
	
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

	
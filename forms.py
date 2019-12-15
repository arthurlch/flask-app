from flask_wtf import Flaskform
from wtforms import Stringfield, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Lenght

"""import flask_wtf: https://flask-wtf.readthedocs.io/en/stable/ 
	import stringfield for displaying a field
	import .validators to include validators as dataRequired(input required from the user),
	Lenght to set a min and max lenght of the Username of the user"""


"""Define the registration form, define a stringfield with an input(Datarequired), and a min-max lenght of the username"""
class RegistrationForm(Flaskform):
	username = Stringfield('Username', 
									validators=[DataRequired(), Lenght(min=2, max=15)])

	email = Stringfield('Email', validators=[Datarequired(), Email()])
	password = PasswordField('Password', validators=[Datarequired()])
	confirm_password = PasswordField('Confirm Password', validators=[Datarequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

class LoginForm(Flaskform):
	
	email = Stringfield('Email', validators=[Datarequired(), Email()])
	password = PasswordField('Password', validators=[Datarequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

	
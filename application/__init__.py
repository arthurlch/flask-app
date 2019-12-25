
""" init.py for package structuration of the app """
from flask import Flask 
# import flask framework 
# import url_for (avoid hard coding of the urls)
from flask_sqlalchemy import SQLAlchemy
# import Bcrypt for pw hashin
from flask_bcrypt import Bcrypt

# python idiom = __name__
app = Flask(__name__)
""" app configuration """
# secret key  16 Characters 16bit key / if public make new
app.config['SECRET_KEY'] ='b88b9d2380bfe69dbb922efa674210a5'
# define database path and location 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# create the dabase and pass app variable to initialize the database
db = SQLAlchemy(app)
# pass app var to initialize the module
bcrypt = Bcrypt(app)

from application import routes
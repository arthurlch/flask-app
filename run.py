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


# from app(file) import app (app variable in __init__)
from application import app 

# python idiom __name_ = '__main__' 
# open file using the terminal ' python3 app.py'
# Terminal run flask OFF 
if __name__ == '__main__':
	app.run(debug=True)	




 	









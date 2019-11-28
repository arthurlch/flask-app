from flask import Flask
app = Flask(__name__)


""" Define the route of the application, route are defined URLS, route can bedefined with a type int str etc  """

@app.route('/')
def index():
 return '<h1>Welcom!</h1>'


""" Server , method that launch the Flask's integrated developement web server """

""" the idiom             if __name = '__main__' 
is used to ensure that the script is launch only when executed directly"""
# debug=True can be changed when the development is over so debug = False then 
if __name__ == '__main__':
 app.run(debug=True)










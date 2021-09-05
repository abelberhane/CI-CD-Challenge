# Setting up Flask and requests to build out the API
from flask import Flask
app = Flask(__name__)

import requests

# The initial landing page and home for my Application
@app.route('/')
def home():
    return '<h1>Welcome to my first REST API.</h1><p>Please go to /hello to view a message.</p>'


# Challenge Task 1.b - Implementing a GET request made to /hello that returns hello world
@app.route('/hello', methods=['GET'])
def hello_world():
    headers = {'HELLO WORLD': 'HELLO WORLD'}
    return 'hello world'







# This was scratched code that I was using to try to change the ports during a testing issue.
#if __name__ == '__main__':
#    app.run(host='127.0.0.1',port=7999, debug=True)
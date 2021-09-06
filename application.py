# Setting up Flask and requests to build out the API
from flask import Flask
from flask import request

app = Flask(__name__)


# The initial landing page and home for my Application
@app.route('/')
def home():
    return '<h1>Welcome to my first REST API.</h1><p>Please go to /hello to view a message.</p>'


# Challenge Task 1.b - Implementing a GET request made to /hello that returns hello world
@app.route('/hello')
def hello_world():
    # headers = {'HELLO WORLD': 'HELLO WORLD'}
    return 'hello world'


# make sure I am listening to port 9001

# This was scratched code that I was using to try to change the ports during a testing issue.
if __name__ == "__main__":
    print('This is running the port assignment side', flush=True)
    app.run(host='0.0.0.0', port=9001)
else:
    print('I am being ran without port assignment', flush=True)

# Setting up Flask and requests to build out the API
from flask import Flask, request, Response

app = Flask(__name__)


# The initial landing page and home for my Application
@app.route('/')
def home():
    return '<h1>Welcome to my first REST API.</h1>' \
           '<p>Please go to /hello to view a message.</p>' \
           '<p>Visit /logparser to upload your logs.</p>'


# Challenge Task 1.b - Implementing a GET request made to /hello that returns hello world
# Challenge task 1.c - Here is also where I expected the HEAD logic to go
@app.route('/hello', methods=['GET', 'HEAD'])
def hello_world():
    # Below was my early failed attempt at adding custom headers.
    # Another thought was to catch the GET methods in an if else statement
    # headers = {'HELLO WORLD': 'HELLO WORLD'}
    return 'hello world'

# Challenge Task 1.d - A route to parse logs and provide only the ones with error messages

@app.route('/logparser', methods=['GET', 'POST'])
def log_parser():
    # The GET method initiates the landing page where you submit the log
    if request.method == 'GET':
        # Creates an HTML form that lets you submit the logs
        text = "<!doctype html><head><title>Log Parser 3000</title></head><body>Please submit your log file here"\
               "<form method=post enctype=multipart/form-data><input type=file name=file><input type=submit value=upload></form></body></html>"
        return text
    else:
        # If there was a file submitted in the form above
        if "file" in request.files:
            # Assigns a variable to the submitted item
            file = request.files["file"]
            # Runs through the submitted log, reads, decodes and splits the lines for only those that have error in it
            return "<br>".join(line for line in file.read().decode().splitlines() if "error" in line.lower())
        return "file parameter was not in request.files"


# Here is where I assign what ports the Flask app is listening on which is 9001
if __name__ == "__main__":
    print('This is running the port assignment side', flush=True)
    app.run(host='0.0.0.0', port=9001)
# This is for testing purposes
else:
    print('I am being ran without port assignment', flush=True)

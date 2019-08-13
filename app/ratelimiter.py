from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World'

@app.route('/test')
def hello_test():
    return 'Hello, Test'

@app.route('/a')
def hello_a():
    return 'Hello, A'
from flask import Flask

application = Flask('myApp')

@application.route('/')
def index():
    return '<h1> Hello World </h1>'

if __name__ == "__main__":
    application.run(debug=True)

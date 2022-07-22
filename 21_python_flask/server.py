from flask import Flask

app = Flask(__name__)


helloString = "<h1>Hello, World!!</h1>" # URL http://127.0.0.1:5000/hello

@app.route("/")
def home():
    return '''<h1 style="color:red"> This is home page </h1>'''

@app.route('/hello')
def hello():
    return helloString

if __name__ == "__main__":

    app.run()
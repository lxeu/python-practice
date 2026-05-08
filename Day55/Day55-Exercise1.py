from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def make_italic(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def make_underline(function):
    def wrapper():
        return f"<un>{function()}</un>"
    return wrapper

@app.route("/")
@make_bold
@make_italic
@make_underline
def hello_world():
    return "<p>Hello World!</p>"

@app.route("/username/<name>")
def say_bye(name):
    return name
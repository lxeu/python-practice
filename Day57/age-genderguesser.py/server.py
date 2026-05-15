from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<p>Enter your name</p>"

@app.route("/guess/<name>")
def guess(name):
    params = {"name": name}
    age_data = requests.get("https://api.agify.io", params=params).json()
    age = age_data["age"]
    gender_data = requests.get("https://api.genderize.io", params=params).json()
    gender = gender_data["gender"]
    return render_template("index.html", name=name, gender=gender, age=age)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
import random

app = Flask(__name__)

number = random.randint(0,9)

@app.route("/")
def home_page():
    return "<h1>Guess a number between 0 and 9</h1>" \
            "<img alt='Ulquiorra Cifer from Bleach' src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWx2b3RnOGYwdnF6OHRvNGs0cjhhazF3YzZnODcwMXR1MDA3OTA2aiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/C9p5OvcSFWrte/giphy.gif'></img>"

@app.route("/<int:guess>")
def guess_page(guess):
    if guess < number:
        return "<h2 style='color: red;''>Too low, try again!</h2>" \
               "<img alt='Ichigo Kurosaki' src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExazlsM3VibTNkNnJxZDVudTZyaHZodThva2l1ejU0NTZ5Ymt3cHFqOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/byTVPe9Cz5RM4/giphy.gif'></img>"
    
    if guess > number:
        return "<h2 style='color: red;''>Too high, try again!</h2>" \
               "<img alt='Ichigo Kurosaki' src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjRrNnozcGQwNDN6bGxobWFmdzhkZTgzZHlhN2YyaGNhN2ZoenF6MCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/KnuGX7IV6cnu0/giphy.gif'></img>"
    
    if guess == number:
        return "<h2 style='color: green;''>You guessed it!</h2>" \
               "<img alt='Byakuya Bankai' src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZDM0N293bDY4MXFxejRrbTIwNHVzZnQzNXUzdXRuZTF1OWJkZzR3NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/djYAfVN0dAtq68wWdc/giphy.gif'></img>"
    
# flask --app Day55-HigherOrLower run --debug
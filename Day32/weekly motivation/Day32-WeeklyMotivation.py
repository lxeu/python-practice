import smtplib
import datetime as dt
import random
from email.message import EmailMessage

my_email = "email"
my_password = "password"

now = dt.datetime.now()
week_day = now.weekday()

if week_day == 5:
    with open("weekly motivation/quotes.txt") as f:
        quotes = f.readlines()
        random_quote = random.choice(quotes)
    msg = EmailMessage()
    msg["Subject"] = "Motivation"
    msg["From"] = my_email
    msg["To"] = "m.wang33@share.epsb.ca"
    msg.set_content(random_quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.send_message(msg)
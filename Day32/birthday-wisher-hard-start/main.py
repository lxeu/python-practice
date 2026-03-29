import datetime as dt
import pandas
import random
import smtplib
from email.message import EmailMessage

now = dt.datetime.now()
month = now.month
day = now.day

birthday = pandas.read_csv("birthday-wisher-hard-start/birthdays.csv")
bday_dict = {
    (row.month, row.day): row
    for (index, row) in birthday.iterrows()
}

if (month, day) in bday_dict:
    person = bday_dict[(month, day)]
    # choose a random birthday letter and replace [NAME]
    with open(f"birthday-wisher-hard-start/letter_templates/letter_{random.randint(1,3)}.txt") as f:
        letter = f.read()
        final_letter = letter.replace("[NAME]", person["name"])

    # email info
    my_email = "email"
    my_password = "password"
    msg = EmailMessage()
    msg["Subject"] = "Happy Birthday!"
    msg["From"] = my_email
    msg["To"] = person["email"]
    msg.set_content(final_letter)

    # send email
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.send_message(msg)

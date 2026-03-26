from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# --------------------------- PASSWORD GENERATOR------------------------------ #
def generate_password():
    password_input.delete(0,END)
    letters = [
        'A','B','C','D','E','F','G','H','I','J','K','L','M',
        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        'a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z'
    ]

    numbers = ['0','1','2','3','4','5','6','7','8','9']

    symbols = [
        '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
        '-', '_', '=', '+', '[', ']', '{', '}', '|',
        ';', ':', "'", '"', ',', '.', '<', '>', '/', '?', '`', '~'
    ]

    letterswanted = random.randint(8,10)
    numberswanted = random.randint(2,4)
    symbolswanted = random.randint(2,4)

    password_letters = [random.choice(letters) for _ in range(letterswanted)]
    password_numbers = [random.choice(numbers) for _ in range(numberswanted)]
    password_symbols = [random.choice(symbols) for _ in range(symbolswanted)]

    password = password_letters + password_numbers + password_symbols

    random.shuffle(password)

    output = "".join(password)
    password_input.insert(0,output)
    pyperclip.copy(output)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    username = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if len(website) < 1 or len(password) < 1 or len(username) < 1:
        messagebox.showinfo(title="Error", message="Don't leave any fields empty!")
    else:
        try:
            with open("password-manager-start improved/saved_passwords.json", mode="r") as f:
                # read old data
                data = json.load(f)

        except (FileNotFoundError, json.JSONDecodeError):
            with open("password-manager-start improved/saved_passwords.json", mode="w") as f:
                json.dump(new_data, f, indent=4)
        else:
            # update old data
            data.update(new_data)
            with open("password-manager-start improved/saved_passwords.json", mode="w") as f:
                # save new data
                json.dump(data, f, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

# --------------------------- Search Info ---------------------------- #

def search():
    website = website_input.get()
    try:
        with open("password-manager-start improved/saved_passwords.json", mode="r") as f:
            data = json.load(f)   
    except FileNotFoundError:
        messagebox.showinfo(title="Alert", message=f"No file found")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Username: {data[website]['username']}\nPassword: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Not Found", message=f"No info for {website} exist.") 


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="password-manager-start improved/logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

# "Website:" _______
website_text = Label(text="Website:")
website_text.grid(row=1,column=0)

# Website: "_______"
website_input = Entry(width=21)
website_input.grid(row=1,column=1)
website_input.focus()
 
# "Email/Username:" _______
email_text = Label(text="Email/Username:")
email_text.grid(row=2,column=0)

# Email/Username: "_______"
email_input = Entry(width=38)
email_input.grid(row=2,column=1,columnspan=2)
email_input.insert(0, "wangmatthew6000@gmail.com")

# "Password:" ____
password_text = Label(text="Password:")
password_text.grid(row=3,column=0)

# Password: "____"
password_input = Entry(width=21)
password_input.grid(row=3,column=1)

# "Generate"
generate_button = Button(text="Generate Password",command=generate_password)
generate_button.grid(row=3,column=2)
# "Generate"
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4,column=1,columnspan=2)

# "Search"
search_button = Button(text="Search", width=13, command=search)
search_button.grid(row=1, column=2)

window.mainloop()
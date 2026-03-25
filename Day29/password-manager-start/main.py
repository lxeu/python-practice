from tkinter import *
from tkinter import messagebox
import random
import pyperclip
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

    if len(website) < 1 or len(password) < 1 or len(username) < 1:
        messagebox.showinfo(title="Error", message="Don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail/Username: {username}\nPassword: {password}\nWould you like to save this information?")
        if is_ok:
            with open("password-manager-start/saved_passwords.txt", mode="a") as f:
                f.write(f"Website: {website}\n")
                f.write(f"Username: {username}\n")
                f.write(f"Password: {password}\n\n")
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="password-manager-start/logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

# "Website:" _______
website_text = Label(text="Website:")
website_text.grid(row=1,column=0)

# Website: "_______"
website_input = Entry(width=38)
website_input.grid(row=1,column=1, columnspan=2)
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

window.mainloop()
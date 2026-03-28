BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

to_learn = {}
current_card = {}

try:
    data = pandas.read_csv("flash-card-project-start/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("flash-card-project-start/data/mandarin_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# Generate new cards
def next_card():
    global current_card, flip_timer
    if len(to_learn) == 0:
        canvas.itemconfig(chinese_word, text="You're done!", fill="black")
        canvas.itemconfig(chinese_text, text="")
        return
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(chinese_text, text="Chinese", fill="black")
    canvas.itemconfig(chinese_word, text=current_card["Mandarin"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, flip_card)

# Create new csv to ONLY store words not yet tested.
def word_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("flash-card-project-start/data/words_to_learn.csv", index=False)
    next_card()

def word_unknown():
    next_card()


def flip_card():
    global current_card
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(chinese_text, text="English", fill="white")
    canvas.itemconfig(chinese_word, text=current_card["English"], fill="white")

window = Tk()
window.title("Flashcards")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Canvas setup with front flash card image
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR,highlightthickness=0)
card_front_img = PhotoImage(file="flash-card-project-start/images/card_front.png")
card_back_img = PhotoImage(file="flash-card-project-start/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
chinese_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
chinese_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0,columnspan=2)

# checkmark
checkmark_img = PhotoImage(file="flash-card-project-start/images/right.png")
checkmark_button = Button(image=checkmark_img, highlightthickness=0, command=word_known)
checkmark_button.grid(row=1,column=0)

# cross
cross_img = PhotoImage(file="flash-card-project-start/images/wrong.png")
cross_button = Button(image=cross_img, highlightthickness=0, command=word_unknown)
cross_button.grid(row=1,column=1)

next_card()

window.mainloop()
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00")
    timer_label.config(text="Timer")
    checkmarks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
reps = 0
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

    

# ------------------------- COUNTDOWN MECHANISM ---------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✓"
        checkmarks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas setup with tomato image
canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="pomodoro-start/tomato.png")
canvas.create_image(100,110, image=tomato_img)
timer_text = canvas.create_text(100,128,text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

# "Timer" text
timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "normal"), bg=YELLOW)
timer_label.grid(row=1, column=2)

# "Start" button
start_button = Button(text="Start", bg=YELLOW, highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=3, column=1)

# "Reset" button
reset_button = Button(text="Reset", bg=YELLOW, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=3, column=3)

# Checkmarks label
checkmarks = Label(text="", font=(FONT_NAME, 30, "normal"), bg=YELLOW, fg=GREEN)
checkmarks.grid(row=4, column=2)

window.mainloop()
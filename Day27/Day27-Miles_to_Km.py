from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=20,pady=20)

miles_input = Entry(width=6)
miles_input.grid(row=1,column=2)

miles_label = Label(text="Miles")
miles_label.grid(row=1,column=3)

is_equal_to_label = Label(text="Is equal to")
is_equal_to_label.grid(row=2,column=1)

converted_km_label = Label(text="0")
converted_km_label.grid(row=3,column=2)

km_label = Label(text="Kilometers")
km_label.grid(row=3,column=3)

def calculate_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    converted_km_label.config(text=km)

calculate_button = Button(text="Calculate",command=calculate_km)
calculate_button.grid(row=4,column=2)

window.mainloop()
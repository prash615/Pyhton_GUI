import tkinter as tk
import tkinter.font as tfont
from tkinter import Entry

window = tk.Tk()
window.title("My Application")
window.minsize(width=400, height=300)

custom_font = tfont.Font(family="Times New Roman", size=14, slant='italic')

label = tk.Label(text="Hello World", font=custom_font)
label.pack()

counter = 0
def function_button():
    global counter
    counter = counter + 1
    label.config(text=f"Thanks for clicking! {counter} times")


btn = tk.Button(text="Click", command=function_button)
btn.pack()


window.mainloop()
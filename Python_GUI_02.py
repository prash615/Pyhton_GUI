import tkinter as tk
import tkinter.font as tfont
from tkinter import Entry

window = tk.Tk()
window.title("My Application")
window.minsize(width=400, height=300)

custom_font = tfont.Font(family="Times New Roman", size=14, slant='italic')

label = tk.Label(text="Hello World", font=custom_font)
label.pack()

def function_button():
    input_txt = user_input.get()
    label.config(text=input_txt)

#taking user ip using Entry()
user_input = Entry(width=30)
user_input.pack()

btn = tk.Button(text="Click", command=function_button)
btn.pack()

window.mainloop()
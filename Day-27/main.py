from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="I am a label")
my_label.pack()

def button_clicked():
    my_label["text"] = input.get()

button = Button(text="Click Me", command=button_clicked)
button.pack()

input = Entry(width=10)
input.pack()






window.mainloop()


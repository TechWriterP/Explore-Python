from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

def miles_to_km():
    miles = miles_input.get()
    km = round(int(miles) * 1.60934, 2)
    miles_label_km_result.config(text=km)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

miles_label_is_equal_to = Label(text= "is equal to")
miles_label_is_equal_to.grid(column=0, row=1)

miles_label_km_result = Label(text= "0")
miles_label_km_result.grid(column=1, row=1)

miles_label_km = Label(text="Km")
miles_label_km.grid(column=2, row=1)


miles_button = Button(text="Calculate", command=miles_to_km)
miles_button.grid(column=1, row=2)

window.mainloop()
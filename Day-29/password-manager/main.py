from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = ""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    password = "".join(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    pswd_entry.delete(0,END)
    pswd_entry.insert(0, password)
    pyperclip.copy(password)

    # print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    user_website = web_entry.get()
    user_email = email_entry.get()
    user_pswd = pswd_entry.get()
    # str_to_save = f"{user_website} | {user_email} | {user_pswd}"

    if len(user_email) == 0 or len(user_pswd) == 0:
        messagebox.showinfo(title="Ooops!", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=user_website, message=f"These are the details entered: \nEmai;: {user_email} \nPassword: {user_pswd}\n\nPress OK to save!")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{user_website} | {user_email} | {user_pswd}\n")
            web_entry.delete(0,END)
            pswd_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

web_label = Label(text="Website: ")
web_label.grid(column=0, row=1)

web_entry = Entry(width=50)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0,"rpa.prashant@gmail.com")

pswd_label = Label(text="Password: ")
pswd_label.grid(column=0, row=3)

pswd_entry = Entry(width=28)
pswd_entry.grid(column=1, row=3)

gen_pswd_btn = Button(text="Generate Password", width=15, command=generate_password)
gen_pswd_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=45, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
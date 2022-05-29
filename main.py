from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = letters_list + symbols_list + numbers_list
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def find_password():
    data_input = website_entry.get().title()

    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")

    else:
        if data_input in data:
            password = data[data_input]["password"]
            email = data[data_input]["email"]
            messagebox.showinfo("info", f"password: {password}\nemail: {email}")
        else:
            messagebox.showerror("not found", f"{data_input} not found")



def save_password():
    email = username_entry.get()
    password = password_entry.get().title()
    website = website_entry.get().title()
    new_data = {website: {
        "email": email,
        "password": password,
    }
    }

    alright = True
    all_items = [email, password, website]
    for i in all_items:
        if len(i) == 0:
            alright = False

    if alright != True:
        messagebox.showinfo(title="Oops!", message="you have left some fields missing")

    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:

            data.update(new_data)

            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            password_entry.delete(0, END)
            website_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# screen

screen = Tk()
screen.title("Password Manager")
screen.config(padx=50, pady=50)

# canvas

canvas = Canvas(height=200, width=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=1, column=2)

# website

website_entry = Entry()
website_entry.focus()
website_entry.config(width=33)
website_entry.grid(row=2, column=2)
website_label = Label(text="Website: ")
website_label.grid(row=2, column=1)

# username/email

username_entry = Entry()
username_entry.insert(0, "sample@gmail.com")
username_entry.config(width=52)
username_entry.grid(row=3, column=2, columnspan=2)
username_label = Label(text="Email/Username: ")
username_label.grid(row=3, column=1)

# password

password_button = Button(text="Generate Password", height=1, padx=0, pady=0, command=generate_password)
password_button.grid(row=4, column=3)
password_entry = Entry()
password_entry.config(width=33)
password_entry.grid(row=4, column=2)
password_label = Label(text="Password: ")
password_label.grid(row=4, column=1)

# buttons

# add button

add_button = Button(text="Add", command=save_password)
add_button.config(width=44)
add_button.grid(row=5, column=2, columnspan=2)

# search button

search_button = Button(text="Search", command=find_password)
search_button.config(width=14)
search_button.grid(row=2, column=3)

screen.mainloop()

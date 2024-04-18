from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def create_pass():
    letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list +=[random.choice(letters) for i in range(nr_letters)]

    password_list += [random.choice(symbols) for i in range(nr_symbols)]

    password_list += [random.choice(symbols) for i in range(nr_symbols)]

    random.shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_input.insert(0,password)
    pyperclip.copy(password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():

    website = web_input.get()
    email = email_input.get()
    password = password_input.get()
    if website == "" or password == "" or email == "":
        messagebox.showerror(title="EROR", message="please fill the forms")

    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"these are the details enterd :\n EMAIL:{email}\nWEBSITE : {website}\nPASSWORD : {password}",
        )
        if is_ok:
            with open("logs.txt", "a") as data:
                data.write(f"{website} | {email} | {password}\n")
                web_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manger")
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website :")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username :")
email_label.grid(column=0, row=2)
password_label = Label(text="Password :")
password_label.grid(column=0, row=3)


# inputs
web_input = Entry(width=40)
web_input.focus()
web_input.grid(column=1, row=1, columnspan=2)
email_input = Entry(width=40)
email_input.insert(0, "hossien.malosi@gmail.com")
email_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# button

gen_button = Button(text="Generate Password",command=create_pass)
gen_button.grid(column=2, row=3)
add_button = Button(text="Add", width=34, command=add_data)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()

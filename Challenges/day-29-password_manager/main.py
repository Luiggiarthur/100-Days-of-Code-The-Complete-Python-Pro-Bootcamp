from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for num in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
def add():
    website_value = website_input.get()
    email_value = email_input.get()
    password_value = password_input.get()

    if len(website_value) == 0 or len(password_value) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure there are not empty fields")
    else:
        is_ok = messagebox.askokcancel(title=website_value, message=f"These are the details entered: "
                                                                    f"\nEmail:{email_value} "
                                                                    f"\nPassword: {password_value} \nIs it o to save?")

        if is_ok:
            with open('data.txt', 'a') as f:
                f.write(f'{website_value} | {email_value} | {password_value} | \n')
            website_input.delete(0,END)
            password_input.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = _label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_input = Entry(window, width=35)
website_input.grid(column=1, row=1, columnspan=2, sticky=EW)
website_input.focus()

email_input = Entry(window, width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky=EW)
email_input.insert(0, "example@gmail.com")

password_input = Entry(window, width=21)
password_input.grid(column=1, row=3, sticky=EW)


generatepass_button = Button(text="Generate Password", command=generate_password)
generatepass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=add)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
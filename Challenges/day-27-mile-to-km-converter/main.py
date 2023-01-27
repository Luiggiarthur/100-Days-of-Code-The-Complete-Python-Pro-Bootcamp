from tkinter import *


def button_clicked():

    mile = float(miles.get())
    km = mile * 1.609

    my_label2.config(text=f"{km}")


window = Tk()
window.title("Mile to Km converter")
#window.minsize(width=300, height=300)
window.config(padx=20, pady=20)
miles = Entry(width=10)
miles.grid(column=1, row=0)

#Label
my_label = Label(text="Miles")
my_label.grid(column=2, row=0)

my_label1 = Label(text="is equal to")
my_label1.grid(column=0, row=1)

my_label2 = Label(text="0")
my_label2.config(text="0")
my_label2.grid(column=1, row=1)

my_label3 = Label(text="Km")
my_label3.grid(column=2, row=1)

#Button

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
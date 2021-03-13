from tkinter import*
from tkinter import messagebox

root = Tk()
root.title("Конвертер")
root.geometry("400x400")


def show_messagebox():
    messagebox.showinfo("Перевод валюты", message.get() + "Yuan = " + str(float(message.get()) * 0.15) + "$")

message = StringVar()
message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.1, anchor="c")

message_button = Button(text="Yuan в $", command=show_messagebox)

message_button.place(relx=.5, rely=.5, anchor="c")

root.mainloop()

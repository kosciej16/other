from tkinter import *

root = Tk()


def log():
    a = e.get()
    s = p.get()
    print(a, s)


label1 = Label(root, text="Username:  ").grid(row=0, column=0)
e = Entry(root, width=50, borderwidth=5, text="Enter Your Username:").grid(row=0, column=2)

label2 = Label(root, text="Password: ").grid(row=1, column=0)
p = Entry(root, width=50, borderwidth=5, text="Enter Your Password:").grid(row=1, column=2)
space = Label(root, text="           ").grid(row=1, column=1)
b = Button(root, text="Login", command=log).grid(row=3, column=2)


root.mainloop()

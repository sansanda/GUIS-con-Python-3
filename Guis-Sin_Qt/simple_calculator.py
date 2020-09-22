from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_add():
    return


# create 10 buttons form 0 to 9
buttons = [Button(root, text=str(i), padx=40, pady=20, command=button_add) for i in range(0,10)]

for i,b in enumerate(buttons):
    if i==0:
        b.grid(row=4 ,column=0)
    b.grid(row=3-int((i-1)/3) ,column=((i-1)%3))

root.mainloop()

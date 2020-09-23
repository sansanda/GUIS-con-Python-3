from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5, state=DISABLED)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

global result

def button_click(param):
    #e.delete(0,END)
    #check if number
    try:
        digit = int(param)
        e.configure(state=NORMAL)
        e.insert(END, digit)
        e.configure(state=DISABLED)
    except ValueError:
        #user click a non number button
        text = e.get()
        if (len(text) == 0):
            #no previous number was entered
            print("no previous number was entered")
            return
        else:
            result = int(text)
            e.configure(state=NORMAL)
            e.insert(END, param)
            e.configure(state=DISABLED)



# create all the buttons
buttons = [Button(root, text=str(i), padx=40, pady=20, command=lambda i=i:  button_click(str(i))) for i in range(0,10)]

buttons.append(Button(root, text="+", padx=40, pady=20, command=lambda: button_click("+")))
buttons.append(Button(root, text="=", padx=40, pady=20, command=lambda: button_click("=")))
buttons.append(Button(root, text="clear", padx=120, pady=20, command=lambda: button_click("clear")))

#distribute the number buttons
for i,b in enumerate(buttons):
    if i==0:
        b.grid(row=4 ,column=0)
        continue
    if (i>0 and i<10):
        b.grid(row=3-int((i-1)/3) ,column=((i-1)%3))

#distribute the rest of the buttons
#the + button
buttons[10].grid(row=4,column=1)
#the = button
buttons[11].grid(row=4,column=2)
#the clear button
buttons[12].grid(row=5,column=0,columnspan=3)


root.mainloop()

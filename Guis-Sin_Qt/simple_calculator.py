from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5, state=DISABLED)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def insertParamInEntry(param, e):

    e.configure(state=NORMAL)
    e.insert(END, param)
    e.configure(state=DISABLED)

def getCalculatorState(param, e):

    e_state = dict()
    param_type = dict()
    operator = '+'

    e_state['e_is_empty'] = False
    e_state['e_has_a_number'] = False
    e_state['e_has_lastcharacter_minus'] = False
    e_state['e_has_lastcharacter_plus'] = False

    param_type['param_is_digit'] = False
    param_type['param_is_plus'] = False
    param_type['param_is_minus'] = False
    param_type['param_is_equal'] = False
    param_type['param_is_clear'] = False

    if len(e.get()) == 0:
        e_state['e_is_empty'] = True
    if str(e.get()).isdigit():
        e_state['e_has_a_number'] = True
    if len(e.get())>0 and e.get()[-1] == '-':
        e_state['e_has_lastcharacter_minus'] = True
    if len(e.get())>0 and e.get()[-1] == '+':
        e_state['e_has_lastcharacter_plus'] = True

    if str(param).isdigit():
        param_type['param_is_digit'] = True
    if param == '+':
        param_type['param_is_plus'] = True
        operator = '+'
    if param == '-':
        param_type['param_is_minus'] = True
        operator = '-'
    if param == '=':
        param_type['param_is_equal'] = True
    if param == 'clear':
        param_type['param_is_clear'] = True

    return e_state, param_type, operator


def button_click(param):

    e_state,param_type,operator = getCalculatorState(param, e)

    if param_type['param_is_clear']:
        e.configure(state=NORMAL)
        e.delete(0, END)
        e.configure(state=DISABLED)
        return

    if e_state['e_is_empty']:
        if not param_type['param_is_digit']: #ask if param is not a digit
            return
        else:
            insertParamInEntry(param,e)
            return
    elif e_state['e_has_a_number']:
        if param_type['param_is_equal']:
            return
        else:
            insertParamInEntry(param,e)
            return
    elif e_state['e_has_lastcharacter_minus'] or e_state['e_has_lastcharacter_plus']:
        if param_type['param_is_digit']:
            insertParamInEntry(param,e)
        return
    else:
        # case dddd[+ or -]dddd
        if param_type['param_is_equal']:
            numbers = str(e.get()).split(operator)
            e.configure(state=NORMAL)
            e.delete(0, END)
            if operator=='+':
                e.insert(0,str(int(numbers[0])+int(numbers[1])))
            elif operator=='-':
                e.insert(0, int(str(numbers[0]) - int(numbers[1])))
            e.configure(state=DISABLED)

        elif param_type['param_is_digit']:
            e.configure(state=NORMAL)
            e.insert(END, param)
            e.configure(state=DISABLED)
        return


# create all the buttons
buttons = [Button(root, text=str(i), padx=40, pady=20, command=lambda i=i: button_click(str(i))) for i in range(0, 10)]

buttons.append(Button(root, text="+", padx=40, pady=20, command=lambda: button_click("+")))
buttons.append(Button(root, text="=", padx=40, pady=20, command=lambda: button_click("=")))
buttons.append(Button(root, text="clear", padx=120, pady=20, command=lambda: button_click("clear")))

# distribute the number buttons
for i, b in enumerate(buttons):
    if i == 0:
        b.grid(row=4, column=0)
        continue
    if (i > 0 and i < 10):
        b.grid(row=3 - int((i - 1) / 3), column=((i - 1) % 3))

# distribute the rest of the buttons
# the + button
buttons[10].grid(row=4, column=1)
# the = button
buttons[11].grid(row=4, column=2)
# the clear button
buttons[12].grid(row=5, column=0, columnspan=3)

root.mainloop()

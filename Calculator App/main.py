from tkinter import *

import ast

root = Tk()

# Functions for equation display and calculation
index = 0 
def get_number(num):
    global index
    display.insert(index, num)
    index+=1

def get_op(op):
    global index
    length = len(op)
    display.insert(index, op)
    index+=length

def clear_all():
    display.delete(0,END)

def calculate():
    equation = display.get()
    try:
        node = ast.parse(equation,mode="eval")
        answer = eval(compile(node, '<string>', 'eval'))
        clear_all()
        display.insert(0,answer)
    except Exception:
        clear_all()
        display.insert(0,"Error")

def delete():
    equation = display.get()
    if len(equation):
        new_equation = equation[:-1]
        clear_all()
        display.insert(0,new_equation)
    else:
        clear_all()
        display.insert(0,"")


display = Entry(root)
display.grid(row=1,columnspan=6)

# Makes a grid of button (0-9) in a grid using a for loop, assigns the get number number to each button with the corresponding value
numbers = [1,2,3,4,5,6,7,8,9]
counter = 0
for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        button = Button(root,text=button_text,width=2,height=2,command=lambda text=button_text: get_number(text))
        button.grid(row=x+2,column=y)
        counter+=1
button0 = Button(root,text=0,width=2,height=2,command=lambda: get_number(0))
button0.grid(row=5,column=1)

# makes a grid of action buttons using a for loop and a list of operations
count = 0
operations = ["+", "-", "*", "/", "*3.14", "%", "(", "**", ")", "**2"] 
for x in range(4):
    for y in range(3):
        if count < len(operations):
            button = Button(root,text=operations[count],width=2,height=2,command=lambda op=operations[count]:get_op(op))
            count+=1
            button.grid(row=x + 2,column=y+3)


Button(root,text="AC",width=2,height=2,command=clear_all).grid(row=5,column=0)
Button(root,text="=",width=2,height=2,command=calculate).grid(row=5,column=2)
Button(root,text=" ",width=2,height=2).grid(row=5,column=4)
Button(root,text="<-",width=2,height=2,command=delete).grid(row=5,column=5)

root.mainloop()
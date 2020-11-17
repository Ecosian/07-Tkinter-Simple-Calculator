from tkinter import*

window= Tk()
window.geometry('250x205+0+0')
window.title("Simple Calculator")
window.resizable(0,0)

def add():
    res=int(num1.get()) + int(num2.get())
    myText.set(res)

def mult():
    res=int(num1.get()) * int(num2.get())
    myText.set(res)

def subt():
    res=int(num1.get()) - int(num2.get())
    myText.set(res)

def divi():
    res=int(num1.get()) / int(num2.get())
    myText.set(res)

myText=StringVar();
Label(window, text="Input 1", font=("Calibri", 20)).grid(row=0, sticky=W)
Label(window, text="Input 2", font=("Calibri", 20)).grid(row=1, sticky=W)
Label(window, text="Result:", font=("Calibri", 20)).grid(row=2, sticky=W)
result=Label(window, text="", textvariable=myText).grid(row=2, column=1, sticky=W)

num1 = Entry(window, width=20)
num1.grid(row=0, column=1)
num2 = Entry(window, width=20)
num2.grid(row=1, column=1)

b = Button(window, text="Addition", font=("Arial", 15), command=add)
b.grid(row=3, column=0, columnspan=1, sticky=W+E+N+S)

b1 = Button(window, text="Multiplication", font=("Arial", 15), command=mult)
b1.grid(row=3, column=1, columnspan=1, sticky=W+E+N+S)

b2 = Button(window, text="Subtraction", font=("Arial", 15), command=subt)
b2.grid(row=5, column=0, columnspan=1, sticky=W+E+N+S)

b3 = Button(window, text="Division", font=("Arial", 15), command=divi)
b3.grid(row=5, column=1, columnspan=1, sticky=W+E+N+S)

window.mainloop()

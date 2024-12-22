# creating an Advance Calculator using tkinter

from tkinter import Tk, Entry, Button, StringVar

class Calculator:

    def __init__(self, master):     # master is the main window
        master.title('Calculator')  # setting the title of the window
        master.geometry('300x400')  # setting the size of the window
        master.resizable(False, False) # making the window non-resizable
        master.config(bg='gray') # setting the background color of the window

        self.equation = StringVar() # creating a string variable to store the equation
        self.entry_value = '' # creating a string variable to store the value of the entry widget
        Entry(master, textvariable=self.equation, font=('Arial', 20), bd=10, insertwidth=4, width=14, bg='powder blue', justify='right').grid(row=0, column=0, columnspan=4) # creating an entry widget to display the equation
        
        Button(width=10, height=3, text='7', command=lambda: self.show(7)).grid(row=1, column=0)
        Button(width=10, height=3, text='8', command=lambda: self.show(8)).grid(row=1, column=1)
        Button(width=10, height=3, text='9', command=lambda: self.show(9)).grid(row=1, column=2)
        Button(width=10, height=3, text='C', command=self.clear).grid(row=1, column=3)
        Button(width=10, height=3, text='4', command=lambda: self.show(4)).grid(row=2, column=0)
        Button(width=10, height=3, text='5', command=lambda: self.show(5)).grid(row=2, column=1)
        Button(width=10, height=3, text='6', command=lambda: self.show(6)).grid(row=2, column=2)
        Button(width=10, height=3, text='/', command=lambda: self.show('/')).grid(row=2, column=3)
        Button(width=10, height=3, text='1', command=lambda: self.show(1)).grid(row=3, column=0)
        Button(width=10, height=3, text='2', command=lambda: self.show(2)).grid(row=3, column=1)
        Button(width=10, height=3, text='3', command=lambda: self.show(3)).grid(row=3, column=2)
        Button(width=10, height=3, text='*', command=lambda: self.show('*')).grid(row=3, column=3)
        Button(width=10, height=3, text='.', command=lambda: self.show('.')).grid(row=4, column=0)
        Button(width=10, height=3, text='0', command=lambda: self.show(0)).grid(row=4, column=1)
        Button(width=10, height=3, text='-', command=lambda: self.show('-')).grid(row=4, column=2)
        Button(width=10, height=3, text='+', command=lambda: self.show('+')).grid(row=4, column=3)
        Button(width=10, height=3, text='(', command=lambda: self.show('(')).grid(row=5, column=0)
        Button(width=10, height=3, text=')', command=lambda: self.show(')')).grid(row=5, column=1)
        Button(width=10, height=3, text='%', command=lambda: self.show('%')).grid(row=5, column=2)
        Button(width=10, height=3, text='^', command=lambda: self.show('**')).grid(row=5, column=3)
        Button(width=10, height=3, text='=', command=self.solve).grid(row=6, column=0, columnspan=4)

    def show(self, value):  # method to concatenate the value of the button clicked to the entry_value
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):  # method to clear the entry widget
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):  # method to evaluate the equation
        result = eval(self.entry_value)
        self.equation.set(result)

root = Tk()

calculator = Calculator(root)

root.mainloop()
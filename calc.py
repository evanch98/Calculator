# Import required libraries
from tkinter import *
import math

def floatInt(numString):
    """Try to change the string into integer first. If it gets error, change the string into float.
    For number string only."""
    try:
        numString = int(numString)
    except ValueError:
        numString = float(numString)
    return numString

# Calculator Logic
class Calculator:
    """Calculator Logic"""
    # Class level variables to store the number throughout the process
    NUM = ''
    num_list = []

    def get_button(self, x):
        """Validating Button Input"""
        if x in '1234567890':
            Calculator.NUM += x
            display['state'] = 'normal'
            display.delete(0, END)
            display.insert(0, Calculator.NUM)
            display['state'] = 'disabled'
        elif x in '+-*/':
            Calculator.num_list.append(Calculator.NUM)
            Calculator.NUM = ''
            Calculator.num_list.append(x)
        elif x == 's':
            Calculator.num_list.append(f'{Calculator.NUM}*{Calculator.NUM}')
            Calculator.NUM = ''
        elif x == 'r':
            Calculator.num_list.append(f'math.sqrt({Calculator.NUM})')
            Calculator.NUM = ''
        elif x == '=':
            Calculator.num_list.append(Calculator.NUM)
            Calculator.NUM = ''
        elif x == 'morp':
            if len(Calculator.NUM) < 1:
                Calculator.NUM = '-'
            else:
                if Calculator.NUM[0] == '-':
                    Calculator.NUM = Calculator.NUM.replace('-', '')
                else:
                    Calculator.NUM = '-' + Calculator.NUM
            display['state'] = 'normal'
            display.delete(0, END)
            display.insert(0, Calculator.NUM)
            display['state'] = 'disabled'
        elif x == 'p':
            Calculator.NUM += '.'
            display['state'] = 'normal'
            display.delete(0, END)
            display.insert(0, Calculator.NUM)
            display['state'] = 'disabled'
        elif x == 'C':
            Calculator.NUM = ''
            Calculator.num_list.clear()
            display['state'] = 'normal'
            display.delete(0, END)
            display['state'] = 'disabled'
        
        print(Calculator.num_list)

    def calculate(self):
        """Calculation using eval()."""
        try:
            result = str(eval(''.join(Calculator.num_list)))
        except Exception:
            result = "Error"

        display['state'] = 'normal'
        display.delete(0, END)
        display.insert(0, str(result))
        display['state'] = 'disabled'

        print(result)

        Calculator.num_list.clear()

# Setting Up Window
root = Tk()
root.geometry("220x210")
root.resizable(0, 0)
root.title('Calculator')
root.iconbitmap('calc.ico')
root.configure(bg='peachpuff')
root.option_readfile('optionDB.txt')

# Initiating Calculator class
one_class = Calculator()

# Display
display = Entry(root)
display.configure(width=25, state=DISABLED)
display.grid(row=0,column=0, columnspan=4, padx=5, pady=5)

# Button Row By Row, Column By Column
clear = Button(root)
clear.configure(text='C', command=lambda: one_class.get_button('C'))
clear.grid(row=1, column=0, padx=5, pady=5)

square = Button(root)
square.configure(text='x²', command=lambda: one_class.get_button('s'))
square.grid(row=1, column=1, padx=5, pady=5)

sqrt = Button(root)
sqrt.configure(text='√x', command=lambda: one_class.get_button('r'))
sqrt.grid(row=1, column=2, padx=5, pady=5)

equal = Button(root)
equal.configure(text='=', command=lambda: [one_class.get_button('='), one_class.calculate()])
equal.grid(row=1, column=3, padx=5, pady=5)

seven = Button(root)
seven.configure(text='7', command=lambda: one_class.get_button('7'))
seven.grid(row=2, column=0, padx=5, pady=5)

eight = Button(root)
eight.configure(text='8', command=lambda: one_class.get_button('8'))
eight.grid(row=2, column=1, padx=5, pady=5)

nine = Button(root)
nine.configure(text='9', command=lambda: one_class.get_button('9'))
nine.grid(row=2, column=2, padx=5, pady=5)

plus = Button(root)
plus.configure(text='+', command=lambda: one_class.get_button('+'))
plus.grid(row=2, column=3, padx=5, pady=5)

four = Button(root)
four.configure(text='4', command=lambda: one_class.get_button('4'))
four.grid(row=3, column=0, padx=5, pady=5)

five = Button(root)
five.configure(text='5', command=lambda: one_class.get_button('5'))
five.grid(row=3, column=1, padx=5, pady=5)

six = Button(root)
six.configure(text='6', command=lambda: one_class.get_button('6'))
six.grid(row=3, column=2, padx=5, pady=5)

minus = Button(root)
minus.configure(text='–', command=lambda: one_class.get_button('-'))
minus.grid(row=3, column=3, padx=5, pady=5)

one = Button(root)
one.configure(text='1', command=lambda: one_class.get_button('1'))
one.grid(row=4, column=0, padx=5, pady=5)

two = Button(root)
two.configure(text='2', command=lambda: one_class.get_button('2'))
two.grid(row=4, column=1, padx=5, pady=5)

three = Button(root)
three.configure(text='3', command=lambda: one_class.get_button('3'))
three.grid(row=4, column=2, padx=5, pady=5)

multiply = Button(root)
multiply.configure(text='×', command=lambda: one_class.get_button('*'))
multiply.grid(row=4, column=3, padx=5, pady=5)

minusOrPlus = Button(root)
minusOrPlus.configure(text='±', command=lambda: one_class.get_button('morp'))
minusOrPlus.grid(row=5, column=0, padx=5, pady=5)

zero = Button(root)
zero.configure(text='0', command=lambda: one_class.get_button('0'))
zero.grid(row=5, column=1, padx=5, pady=5)

point = Button(root)
point.configure(text='.', command=lambda: one_class.get_button('p'))
point.grid(row=5, column=2, padx=5, pady=5)

division = Button(root)
division.configure(text='÷', command=lambda: one_class.get_button('/'))
division.grid(row=5, column=3, padx=5, pady=5)

root.mainloop()

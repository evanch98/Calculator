# Import required libraries
from tkinter import (
    Tk,
    Button,
    Entry
)
import math

# Calculator Logic
class Calculator:
    """Validate the buttons by the get_button method, then calculate the result using the eval() function.
    display_entry method displays the text in the entries."""
    def __init__(self):
        """Initializing Calculator class with two attributes to store numbers."""
        self.num = ''
        self.num_list = []
    
    def display_entry(self, entries, text):
        """This function displays the text in the entries."""
        entries['state'] = 'normal'
        entries.delete(0, 'end')
        entries.insert(0, text)
        entries['state'] = 'disabled'

    def get_button(self, x):
        """Validating Button Input"""
        if x in '1234567890':
            self.num  += x
            self.display_entry(entries=display, text=self.num)
        elif x in '+-*/':
            self.num_list.append(self.num)
            self.num = ''
            self.num_list.append(x)
        elif x == 's':
            self.num_list.append(f"{self.num}*{self.num}")
            self.num = ''
        elif x == 'r':
            self.num_list.append(f'math.sqrt({self.num})')
            self.num = ''
        elif x == '=':
            self.num_list.append(self.num)
            self.num = ''
        elif x == 'morp':
            if len(self.num) < 1:
                self.num = '-'
            else:
                if self.num[0] == '-':
                    self.num = self.num.replace('-', '')
                else:
                    self.num = '-' + self.num
            self.display_entry(entries=display, text=self.num)
        elif x == 'p':
            self.num += '.'
            self.display_entry(entries=display, text=self.num)
        elif x == 'C':
            self.num = ''
            self.num_list.clear()
            self.display_entry(entries=display, text='')
        
        print(self.num_list)

    def calculate(self):
        """Calculation using eval()."""
        try:
            result = str(eval(''.join(self.num_list)))
        except Exception:
            result = "Error"

        self.num = result
        
        self.display_entry(entries=display, text=self.num)

        print(result)

        self.num_list.clear()

# Setting Up Window
root = Tk()
root.geometry("220x210")
root.resizable(0, 0)
root.title('Calculator')
root.iconbitmap('calc.ico')
root.configure(bg='peachpuff')
root.option_readfile('optionDB.txt')

# Initiating Calculator class
calc = Calculator()

# Display
display = Entry(root)
display.configure(width=25, state='disabled')
display.grid(row=0,column=0, columnspan=4, padx=5, pady=5)

def buttons(text, command, row_num, column_num):
    """Button configuration."""
    button = Button(root)
    if text == '=':
        button.configure(text=text, command=lambda: [calc.get_button(command), calc.calculate()])
    else:
        button.configure(text=text, command=lambda: calc.get_button(command))
    button.grid(row=row_num, column=column_num, padx=5, pady=5)

# Button Row By Row, Column By Column
buttons(text='C', command='C', row_num=1, column_num=0)     # Clear
buttons(text='x??', command='s', row_num=1, column_num=1)    # Square
buttons(text='???x', command='r', row_num=1, column_num=2)    # Square Root
buttons(text='=', command='=', row_num=1, column_num=3)     # Equal
buttons(text='7', command='7', row_num=2, column_num=0)     # Seven
buttons(text='8', command='8', row_num=2, column_num=1)     # Eight
buttons(text='9', command='9', row_num=2, column_num=2)     # Nine
buttons(text='+', command='+', row_num=2, column_num=3)     # Plus
buttons(text='4', command='4', row_num=3, column_num=0)     # Four
buttons(text='5', command='5', row_num=3, column_num=1)     # Five
buttons(text='6', command='6', row_num=3, column_num=2)     # Six
buttons(text='???', command='-', row_num=3, column_num=3)     # Minus
buttons(text='1', command='1', row_num=4, column_num=0)     # One
buttons(text='2', command='2', row_num=4, column_num=1)     # Two
buttons(text='3', command='3', row_num=4, column_num=2)     # Three
buttons(text='??', command='*', row_num=4, column_num=3)     # Multiply
buttons(text='??', command='morp', row_num=5, column_num=0)  # Minus or Plus
buttons(text='0', command='0', row_num=5, column_num=1)     # Zero
buttons(text='.', command='p', row_num=5, column_num=2)     # Decimal
buttons(text='??', command='/', row_num=5, column_num=3)     # Divide

root.mainloop()

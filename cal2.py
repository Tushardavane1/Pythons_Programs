from tkinter import *

root = Tk()

# Text input area
e = Entry(root, width=35, borderwidth=5)
#e.grid(row=0, column=0, columnspan=3, padx=30)
e.pack()
list_of_numbers = []


# Function to get numbers
def number_input(number):
    current_value = e.get()
    e.delete(0, END)
    e.insert(0, str(current_value) + str(number))


def clear_values():
    list_of_numbers.clear()
    e.delete(0, END)


def calculate_result(operation):
    num1 = e.get()
    list_of_numbers.append(float(num1))
    e.delete(0, END)

    if operation == "sum":
        result = sum(list_of_numbers)
    elif operation == "sub":
        result = list_of_numbers[0] - sum(list_of_numbers[1:])
    elif operation == "mul":
        result = 1
        for value in list_of_numbers:
            result *= value
    elif operation == "div":
        result = list_of_numbers[0] / (list_of_numbers[1:])
    elif operation == "mod":
        result = list_of_numbers[0] % (list_of_numbers[1:])
    else:
        result = 0

    e.insert(0, result)


def equals():
    calculate_result("")


# Buttons 9-0, add button, clear, equals
buttn9 = Button(root, text="9", padx=40, pady=20, command=lambda: number_input(9))
buttn9.pack(padx=23,pady=43)
buttn8 = Button(root, text="8", padx=40, pady=20, command=lambda: number_input(8))
buttn8.pack(padx=23,pady=43)
buttn7 = Button(root, text="7", padx=40, pady=20, command=lambda: number_input(7))
buttn7.pack()

buttn6 = Button(root, text="6", padx=40, pady=20, command=lambda: number_input(6))
buttn6.pack()
buttn5 = Button(root, text="5", padx=40, pady=20, command=lambda: number_input(5))
buttn5.pack()
buttn4 = Button(root, text="4", padx=40, pady=20, command=lambda: number_input(4))
buttn4.pack()

buttn3 = Button(root, text="3", padx=40, pady=20, command=lambda: number_input(3))
buttn3.pack()
buttn2 = Button(root, text="2", padx=40, pady=20, command=lambda: number_input(2))
buttn2.pack()
buttn1 = Button(root, text="1", padx=40, pady=20, command=lambda: number_input(1))
buttn1.pack()

buttn0 = Button(root, text="0", padx=40, pady=20, command=lambda: number_input(0))
buttn0.pack()
buttn_add = Button(root, text="+", padx=40, pady=20, command=lambda: calculate_result("sum"))
buttn_add.pack()
buttn_sub = Button(root, text="-", padx=40, pady=20, command=lambda: calculate_result("sub"))
root.mainloop()
#Kevin Jonson - XII RPL 4 - 16
# Import necessary modules
from tkinter import *
from tkinter import ttk

# Define function to convert string to ASCII
def str_to_ascii(string):
    ascii_list = []
    for char in string:
        ascii_list.append(ord(char))
    return ascii_list

# Define function to convert between binary, decimal, octal, and hexadecimal
def base_conversion(number, from_base, to_base):
    if from_base == "Decimal":
        decimal_num = int(number)  
    elif from_base == "Binary":
        decimal_num = int(number, 2)
    elif from_base == "Octal":
        decimal_num = int(number, 8)
    elif from_base == "Hexadecimal":
        decimal_num = int(number, 16)
    else:
        raise ValueError("Invalid input base")

    if to_base == "Decimal":
        return str(decimal_num)
    elif to_base == "Binary":
        return bin(decimal_num)[2:]
    elif to_base == "Octal":
        return oct(decimal_num)[2:]
    elif to_base == "Hexadecimal":
        return hex(decimal_num)[2:]
    else:
        raise ValueError("Invalid output base")

# Define function to convert between binary, decimal, octal, and hexadecimal
def convert_base():
    # Get user input
    number = input_entry.get()
    from_base = from_base_choice.get()
    to_base = to_base_choice.get()

    # Convert number
    converted_number = base_conversion(number, from_base, to_base)

    # Display result
    result_label.config(text=converted_number)

# Define function to convert string to ASCII
def convert_ascii():
    # Get user input
    string = input_entry.get()

    # Convert string to ASCII
    ascii_list = str_to_ascii(string)

    # Display result
    result_label.config(text=str(ascii_list))

# Set up the GUI
root = Tk()
root.title("Kevin Jonson")
root.geometry("700x350")

# Create input label and entry box
input_label = ttk.Label(root, text="Insert something")
input_label.pack(pady=10)

input_entry = ttk.Entry(root, width=30)
input_entry.pack()

# Create "Convert" button
convert_button = ttk.Button(root, text="Convert", command=convert_base)
convert_button.pack(pady=10)

# Create "Convert to ASCII" button
ascii_button = ttk.Button(root, text="Convert ke ASCII", command=convert_ascii)
ascii_button.pack(pady=10)

# Create "From base" dropdown menu
from_base_label = ttk.Label(root, text="Convert dari:")
from_base_label.pack(pady=10)

from_base_choice = ttk.Combobox(root, values=["Decimal", "Binary", "Octal", "Hexadecimal"])
from_base_choice.current(0)
from_base_choice.pack()

# Create "To base" dropdown menu
to_base_label = ttk.Label(root, text="Convert ke:")
to_base_label.pack(pady=10)

to_base_choice = ttk.Combobox(root, values=["Decimal", "Binary", "Octal", "Hexadecimal"])
to_base_choice.current(0)
to_base_choice.pack()

# Create result label
result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()

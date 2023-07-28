import json
import tkinter
import customtkinter


with open('./data.json', 'r') as file:
    values = json.load(file)


curr_ids = list(values.keys())


def convert(frm, to, val):
    scl = values[frm]['val']
    inr = scl * val
    scl = values[to]['val']
    return inr / scl


root = customtkinter.CTk()
root.title("Currency Converter")


title = customtkinter.CTkLabel(root, text="Currency Converter", font=('Arial', 18))
title.grid(row=0, column=0, columnspan=5, pady=20)


from_label = customtkinter.CTkLabel(root, text='From: ')
from_label.grid(row=1, column=0, pady=10, padx=10)

from_curr = tkinter.StringVar(root)
from_curr.set(curr_ids[0])
from_curr_option = customtkinter.CTkOptionMenu(root, variable=from_curr, values=curr_ids)
from_curr_option.grid(row=1, column=1, pady=10, padx=10)

from_val = tkinter.StringVar(root)
from_val.set('')
from_val_entry = customtkinter.CTkEntry(root, textvariable=from_val)
from_val_entry.grid(row=2, column=0, columnspan=2, pady=10)


middle_empty_space = customtkinter.CTkLabel(root, text=' ', width=20)
middle_empty_space.grid(row=1, column=2)


to_label = customtkinter.CTkLabel(root, text='To: ')
to_label.grid(row=1, column=3, pady=10, padx=10)

to_curr = tkinter.StringVar(root)
to_curr.set(curr_ids[1])
to_curr_option = customtkinter.CTkOptionMenu(root, variable=to_curr, values=curr_ids)
to_curr_option.grid(row=1, column=4, pady=10, padx=10)

to_val = tkinter.StringVar(root)
to_val.set('')
to_val_label = customtkinter.CTkLabel(root, textvariable=to_val)
to_val_label.grid(row=2, column=3, columnspan=2, pady=10)


def exe_convert():
    to_val.set(str(round(convert(from_curr.get(), to_curr.get(), int(from_val.get())), 2)))


conv_button = customtkinter.CTkButton(root, text='Convert', command=lambda: exe_convert())
conv_button.grid(row=3, column=0, columnspan=5, pady=10)


root.mainloop()

# print(f'{values[to]["sym"]} {"%.2f" % res_curr}')
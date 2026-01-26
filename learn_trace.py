
import tkinter as tk

root = tk.Tk()
root.geometry('1000x400')
root.title('Character Counter')
root.config(background = '#0cf7e0')

text_var = tk.StringVar()
cout_var = tk.StringVar(value = "Total Character : 0")

def count_char(*args):
    data = text_var.get()
    len_data = len(data)
    cout_var.set(f'Total Character : {len_data}')

text_var.trace_add("write", count_char)

ent = tk.Entry(root, font = ('Comic Sans MS' ,35), textvariable = text_var)
ent.pack(pady = 40)


lbl = tk.Label(root, textvariable = cout_var, font = ('Comic Sans MS' ,35))
lbl.pack()


root.mainloop()
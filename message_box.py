import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.geometry('1000x700')
app.title('Messagebox')
app.config(background = '#29d668')

lbl1 = tk.Label(app, text = 'Tkinter Messagebox', font = ('Comic Sans MS' ,40, 'bold'), fg = 'white', bg = '#068a26')
lbl1.pack(fill = 'x')

def show_info():
    messagebox.showinfo("Data Saved", "Your Data Saved Sucessfuly In Database.")

def show_warning():
    messagebox.showwarning("Data Warrning", "Enter Vaid Data")

def show_error():
    messagebox.showerror("Wrong", "Something Went Wrong.")

def yes_no():
    result = messagebox.askyesno("Gym", "You Wana go to GYM")
    
    if result:
        messagebox.showinfo("Yes", "You press Yes")
    else:
        messagebox.showerror("No", "You Press No")

def ok_cnl():
    x = messagebox.askokcancel("Lenrning", "Do you wana learn Python.")
    print(x)

def rety():
    y = messagebox.askretrycancel("No DOne", "Do you wana retry to save dat")
    print(y)

def ync():
    z = messagebox.askyesnocancel("Learn Tkinter", "You you wana learn Tkinter In Detail.")
    print(z)

tk.Button(app, text = "Show Info", command = show_info).pack(pady = 10)
tk.Button(app, text = "Show Warning", command = show_warning).pack(pady = 10)
tk.Button(app, text = "Show Errors", command = show_error).pack(pady = 10)

tk.Button(app, text = "Ask Yes Or No", command = yes_no).pack(pady = 10)

tk.Button(app, text = "Ask ok or Cancel", command = ok_cnl).pack(pady = 10)

tk.Button(app, text = "Retey or Cancel", command = rety).pack(pady = 10)

tk.Button(app, text = "Yes No Cancel", command = ync).pack(pady = 10)





app.mainloop()
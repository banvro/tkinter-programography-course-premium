import tkinter as tk

app = tk.Tk()
app.geometry('1000x500')
app.title('Age Calculator')
app.config(background = '#29d668')

lbl1 = tk.Label(app, text = 'CheckButton Selection', font = ('Comic Sans MS' ,40, 'bold'), fg = 'white', bg = '#068a26')
lbl1.pack(fill = 'x', pady = 30)

# def my_hoblies():
#     my_hobi = []
    
#     if si.get() == 1 : my_hobi.append("Singing")
#     if co.get() == 1 : my_hobi.append("Coding")
#     if cr.get() == 1 : my_hobi.append("Cricket")
#     if fl.get() == 1 : my_hobi.append("Football")
#     if ot.get() == 1 : my_hobi.append("Other")

#     print(my_hobi)


# si = tk.IntVar()
# co = tk.IntVar()
# cr = tk.IntVar()
# fl = tk.IntVar()
# ot = tk.IntVar()

# def my_hoblies():
#     print(si.get())


# si = tk.BooleanVar()
# co = tk.BooleanVar()
# cr = tk.BooleanVar()
# fl = tk.BooleanVar()
# ot = tk.BooleanVar()

def my_hoblies():
    print(si.get())


si = tk.StringVar(value = "No")
co = tk.StringVar(value = "No")
cr = tk.StringVar(value = "yes")
fl = tk.StringVar(value = "No")
ot = tk.StringVar(value = "yes")


tk.Label(app, text = "Your Hobbies").pack()

tk.Checkbutton(app, text = "Singing", variable = si, onvalue = "yes", offvalue = "No").pack()
tk.Checkbutton(app, text = "Coding", variable = co, onvalue = "yes", offvalue = "No").pack()
tk.Checkbutton(app, text = "Cricket", variable = cr, onvalue = "yes", offvalue = "No").pack()
tk.Checkbutton(app, text = "Football", variable = fl, onvalue = "yes", offvalue = "No").pack()
tk.Checkbutton(app, text = "Other", variable = ot, onvalue = "yes", offvalue = "No").pack()

tk.Button(app, text = "My Hobbies", command = my_hoblies).pack(pady = 20)

app.mainloop()
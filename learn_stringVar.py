import tkinter as tk

app = tk.Tk()
app.geometry('1000x420')
app.title('Age Calculator')
app.config(background = '#29d668')

lbl1 = tk.Label(app, text = 'Learn StringVar()', font = ('Comic Sans MS' ,40, 'bold'), fg = 'white', bg = '#068a26')
lbl1.pack(fill = 'x', pady = 30)


var_x = tk.StringVar()

# var_x.set("Hellow world")

en1 = tk.Entry(app, textvariable = var_x)
en1.pack(pady = 30)

lbl = tk.Label(app, textvariable = var_x)
lbl.pack()





app.mainloop()
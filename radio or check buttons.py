import tkinter as tk

app = tk.Tk()
app.geometry('1000x420')
app.title('Age Calculator')
app.config(background = '#29d668')

lbl1 = tk.Label(app, text = 'RadioButton || CheckButton', font = ('Comic Sans MS' ,40, 'bold'), fg = 'white', bg = '#068a26')
lbl1.pack(fill = 'x', pady = 30)

def selected(x):
    print('You selcted : ', x)

tk.Radiobutton(app,
        text = "Male",
        font = ('Comic Sans MS' ,20, 'bold'),
        fg = 'green', bg = 'orange',
        activeforeground = 'red',
        activebackground = 'yellow',
        indicatoron = True,
        anchor = "w",
        width = 25,
        command = lambda: selected("Male")

).pack()


tk.Checkbutton(app,
        text = "Female",
        font = ('Comic Sans MS' ,20, 'bold'),
        fg = 'green', bg = 'orange',
        activeforeground = 'red',
        activebackground = 'yellow',
        indicatoron = True,
        anchor = "w",
        width = 25,
        command = lambda: selected("Female")

).pack(pady = 20)













app.mainloop()
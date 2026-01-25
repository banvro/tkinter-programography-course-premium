import tkinter as tk

app = tk.Tk()
app.geometry('1000x420')
app.title('Age Calculator')
app.config(background = '#29d668')



lbl1 = tk.Label(app, text = 'Learn Padding Nicely', font = ('Comic Sans MS' ,40, 'bold'), fg = 'white', bg = '#068a26')

lbl1.pack(pady = 30, fill = 'x', padx = 50, ipady = 40)

btn = tk.Button(app, text = "click me")
btn.pack(ipadx = 50, ipady = 40)


app.mainloop()
import tkinter as tk

app = tk.Tk()
app.geometry('1000x700')
app.title('Age Calculator')
app.config(background = '#29d668')

def what_choose():
    g = gender.get()
    s = status.get()

    if s:
        print("Marid", g)
    else:
        print("UnMaried", g)




lbl1 = tk.Label(app, text = 'RadioButton Selection', font = ('Comic Sans MS' ,40, 'bold'), fg = 'white', bg = '#068a26')
lbl1.pack(fill = 'x', pady = 30)

gender = tk.StringVar(value = "Male")
status = tk.BooleanVar(value = False)

tk.Label(app, text = "Choose Gender", font = ('Comic Sans MS' ,20, 'bold'),).pack()

tk.Radiobutton(app, text = "Male", value = "Male", variable = gender).pack()
tk.Radiobutton(app, text = "Female", value = "Female", variable = gender).pack()
tk.Radiobutton(app, text = "Other", value = "Other", variable = gender).pack()

tk.Label(app, text = "Choose Status", font = ('Comic Sans MS' ,20, 'bold')).pack()

tk.Radiobutton(app, text = "Maried", value = True, variable = status).pack()
tk.Radiobutton(app, text = "Signle", value = False, variable = status).pack()


tk.Button(app, text = "What Choose", command = what_choose).pack(pady = 20)



def which_fruit():
    f = Fruits.get()
    print(f)

Fruits = tk.IntVar(value = 3)


tk.Label(app, text = "Choose Fruits", font = ('Comic Sans MS' ,20, 'bold'),).pack()

tk.Radiobutton(app, text = "Apple", value = 1, variable = Fruits, command = which_fruit).pack()
tk.Radiobutton(app, text = "Banana", value = 2, variable = Fruits, command = which_fruit).pack()
tk.Radiobutton(app, text = "Grapes", value = 3, variable = Fruits, command = which_fruit).pack()
tk.Radiobutton(app, text = "Mango", value = 4, variable = Fruits, command = which_fruit).pack()











app.mainloop()
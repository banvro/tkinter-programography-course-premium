import tkinter as tk

app = tk.Tk()
app.geometry("800x450")
app.title("Learn Lables")
app.config(background = '#32f714')

lbl = tk.Label(app, text = 'Learn Entry', font = ("Comic Sans MS", 50, 'bold'),fg ='#32f714',bg = '#189605',underline = 6,pady = 20,relief = 'groove',bd = 20)
lbl.pack(side = "top", fill = 'x')



def only_digit(value):
    return value.isdigit() or value == ""

number_validate = (app.register(only_digit), "%P")



ent = tk.Entry(app,
            font = ("Arial", 30),
            fg = 'green',
            bg = '#b5f772',
            justify = 'left',
            width = 24,
            relief = 'sunken',     #flat, raised, sunken, ridge, groove
            bd = 10,
            insertbackground = 'red',
            insertwidth = 6,
            state = 'normal',
            selectbackground = 'yellow',
            selectforeground = 'red',
            # show = "*",
            validate = 'key',
            validatecommand = number_validate
)

ent.pack(pady = 20)








app.mainloop()
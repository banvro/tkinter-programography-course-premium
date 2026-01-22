import tkinter as tk

app = tk.Tk()
app.geometry("800x450")
app.title("Learn Lables")
app.config(background = '#32f714')

lbl = tk.Label(app, text = 'Learn Button', font = ("Comic Sans MS", 50, 'bold'),fg ='#32f714',bg = '#189605',underline = 6,pady = 20,relief = 'groove',bd = 20)
lbl.pack(side = "top", fill = 'x')


def hitme():
    print("Button Clicked...")



btn = tk.Button(app, 
                text = 'Click Me',
                font = ('Courier', 30, 'bold'),
                fg = 'white',
                bg = 'darkgreen',
                underline = 0, 
                padx = 30,
                relief = 'raised',
                bd = 10,
                activebackground = 'yellow',
                activeforeground = 'red',   
                # width = 13,
                # height = 6,
                cursor = 'hand2',
                anchor = "center",
                command = hitme



)
btn.pack(pady = 30)









app.mainloop()
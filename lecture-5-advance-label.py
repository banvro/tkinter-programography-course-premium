
import tkinter as tk

app = tk.Tk()
app.geometry("700x450")
app.title("Learn Lables")
app.config(background = '#32f714')

lbl = tk.Label(app, text = 'Hellow world', font = ("Arial", 50, 'bold'),fg ='#32f714',bg = '#189605',underline = 5,pady = 20,relief = 'groove',bd = 20)
lbl.pack(side = "top", fill = 'x')

lbl1 = tk.Label(app, 
    text = "I am learning Tkinter To build Desktop Applications.",
    font = ('Courier', 26),
    wraplength = 500,
    width = 30,
    height = 7,
    justify = 'left',
    cursor = "hand2",
    anchor = "nw"
    )

lbl1.pack()

app.mainloop()
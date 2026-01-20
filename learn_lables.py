
import tkinter as tk

app = tk.Tk()
app.geometry("700x400")
app.title("Learn Lables")
app.config(background = '#32f714')


lbl = tk.Label(app, 
            text = 'Hellow world', 
            font = ("Arial", 50, 'bold'),
            fg = '#32f714',
            bg = '#189605',
            underline = 5,
            pady = 20,
            relief = 'groove',
            bd = 20
            )

    # flat, raised, sunken, ridge, groove

lbl.pack(side = "top", fill = 'x')


app.mainloop()
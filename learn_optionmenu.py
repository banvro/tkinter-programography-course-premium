import tkinter as tk

app = tk.Tk()
app.geometry("900x500")
app.title("Learn Dropdown")
app.config(background = '#32f714')

lbl = tk.Label(app, text = 'Simple Dropdown', font = ("Arial", 50, 'bold'),fg ='#32f714',bg = '#189605',underline = 5,pady = 20,relief = 'groove',bd = 20)
lbl.pack(side = "top", fill = 'x')

options = ["Python", "Java", "javascript", "Modulo", "PHP", "Swift", "Go"]

slected_lan = tk.StringVar()
slected_lan.set("Select a Language")

def selected_item():
    print(slected_lan.get())

drop = tk.OptionMenu(app, slected_lan, *options)
drop.config(font = ("Arial", 20))
drop["menu"].config(font = ("Arial", 20))

drop.pack(pady = 30)




tk.Button(app, text = "Slected Langauge", command = selected_item).pack()




app.mainloop()
import tkinter as tk

app = tk.Tk()
app.geometry("500x500")


lb = tk.Listbox(app, font = ("Arial", 20), bg = "#edfc5d", selectbackground = 'green', selectforeground = "white")
lb.pack(pady = 40)


lb.insert(tk.END, "Python")
lb.insert(tk.END, "JavaScript")
lb.insert(tk.END, "Java")
lb.insert(tk.END, "PHP")
lb.insert(tk.END, "Swift")


lb.select_set(1)
lb.select_set(2)
lb.select_set(4)

def selcted_item():
    inx = lb.curselection()
    if inx:
        print(lb.get(inx))

tk.Button(app, text = "My Selection", command = selcted_item).pack()


app.mainloop()


# Notes: https://miro.com/app/board/uXjVGESMQpo=/?share_link_id=913440573045
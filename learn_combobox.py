import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.title("Combobox Dropdown")
app.geometry("400x250")

options = ["India", "USA", "Canada", "Germany", "France", "Indonesia"]

selected = tk.StringVar()

combo = ttk.Combobox(app, values = options, textvariable = selected, state = "readonly")
combo.pack(pady = 40)

combo.set("Choose a Country")


def selected_item():
    print(selected.get())


tk.Button(app, text = "Choosed Country", command = selected_item).pack(pady = 40)





app.mainloop()




# https://miro.com/app/board/uXjVGEKMN00=/?share_link_id=158356777790
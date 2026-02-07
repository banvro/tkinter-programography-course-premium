import tkinter as tk

app = tk.Tk()
app.geometry("500x500")

lst = ['apple', 'banana', 'cherry', 'mango', 'orange', 'strawberry']

lb = tk.Listbox(app, font = ("Arial", 20), bg = "#edfc5d", selectbackground = 'green', selectforeground = "white", selectmode = "extended")
lb.pack(pady = 40)

for i in lst:
    lb.insert(tk.END, i)


def my_slections():
    indexs = lb.curselection()
    zx = []

    for i in indexs:
        zx.append(lb.get(i))
    
    print(zx)

def clear_items():
    lb.select_clear(0, tk.END)

def delete_item():
    index = lb.curselection()

    if index:
        lb.delete(index)


tk.Button(app, text = "My Selection", command = my_slections).pack()

tk.Button(app, text = "Clear Selection", command = clear_items).pack(pady = 20)

tk.Button(app, text = "Delete Item", command = delete_item).pack()

app.mainloop()



# Notes: https://miro.com/app/board/uXjVGESMQpo=/?share_link_id=913440573045
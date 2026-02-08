import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.geometry('600x650')
app.title("My Todo App")
app.config(background = '#9cffd4')

tk.Label(app, text = '📝 To-Do List', font = ('Arial', 30, 'bold'), background = '#9cffd4').pack(pady = 20)

ent = tk.Entry(app, font = ('Arial', 24), width = 25)
ent.pack()

def adding_task():
    task = ent.get()
    if task == "":
        messagebox.showwarning("Empty", "Please Enter Task First.")
    else:
        my_todos.insert(tk.END, task)
        ent.delete(0, tk.END)


tk.Button(app, text = "Add Task", font = ('Arial', 16, 'bold'), bg = 'green', fg = 'white', command = adding_task).pack(pady = 20)


my_todos = tk.Listbox(app, width = 40, height = 10, font = ("Arial", 18))
my_todos.pack()



def deleting_todo():
    indexx = my_todos.curselection()
    if indexx:
        my_todos.delete(indexx)
    else:
        messagebox.showerror("Choose Somethong", "Choose a task you wana delete.")

def clear_all_task():
    my_todos.delete(0, tk.END)


tk.Button(app, text = "Delete Task", font = ('Arial', 16, 'bold'), bg = 'red', fg = 'white', command = deleting_todo).pack(pady = 20)

tk.Button(app, text = "Clear Tasks", font = ('Arial', 16, 'bold'), bg = 'blue', fg = 'white', command = clear_all_task).pack()


app.mainloop()



# Notes : https://miro.com/app/board/uXjVGDhZhqU=/?share_link_id=38180177539

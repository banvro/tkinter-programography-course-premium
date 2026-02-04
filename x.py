import tkinter as tk

root = tk.Tk()
root.title("All Variables Example")
root.geometry("350x300")


tk.Radiobutton(root, text="Male",  value=1).pack()
tk.Radiobutton(root, text="Female",  value=2).pack()
tk.Radiobutton(root, text="Other",  value=3).pack()


root.mainloop()

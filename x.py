import tkinter as tk

root = tk.Tk()
root.title("StringVar with Checkbutton")
root.geometry("350x200")

notifications = tk.StringVar(value="OFF")

def show_status():
    lbl.config(text="Notifications: " + notifications.get())

tk.Checkbutton(
    root,
    text="Enable Notifications",
    variable=notifications,
    onvalue="ON ✅",
    offvalue="OFF ❌",
    command=show_status
).pack(pady=20)

lbl = tk.Label(root, text="Notifications: OFF ❌", fg="blue")
lbl.pack()

root.mainloop()

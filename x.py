import tkinter as tk

root = tk.Tk()
root.title("App Settings")

dark_mode = tk.IntVar()
auto_save = tk.IntVar()
notifications = tk.IntVar()
location_access = tk.IntVar()

def apply_settings():
    print("Dark Mode:", dark_mode.get())
    print("Auto Save:", auto_save.get())
    print("Notifications:", notifications.get())
    print("Location Access:", location_access.get())

tk.Label(root, text="Enable settings:").pack(pady=5)

tk.Checkbutton(root, text="Dark Mode", variable=dark_mode).pack(anchor="w")
tk.Checkbutton(root, text="Auto Save", variable=auto_save).pack(anchor="w")
tk.Checkbutton(root, text="Notifications", variable=notifications).pack(anchor="w")
tk.Checkbutton(root, text="Location Access", variable=location_access).pack(anchor="w")

tk.Button(root, text="Apply", command=apply_settings).pack(pady=10)

root.mainloop()

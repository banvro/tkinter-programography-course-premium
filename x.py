import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.geometry("500x400")
app.title("MessageBox Demo")

def info_msg():
    messagebox.showinfo("Information", "This is an info message!")

def warning_msg():
    messagebox.showwarning("Warning", "This is a warning message!")

def error_msg():
    messagebox.showerror("Error", "This is an error message!")

def ask_yes_no():
    ans = messagebox.askyesno("Confirm", "Do you want to continue?")
    print(ans, "eeeeeeeeeee")
    if ans:
        messagebox.showinfo("Result", "You clicked YES")
    else:
        messagebox.showinfo("Result", "You clicked NO")

def ask_ok_cancel():
    ans = messagebox.askokcancel("Confirm", "Are you sure?")
    print("OK Cancel Answer:", ans)

def ask_retry_cancel():
    ans = messagebox.askretrycancel("Failed", "Retry again?")
    print("Retry Cancel Answer:", ans)

def ask_yes_no_cancel():
    ans = messagebox.askyesnocancel("Save File", "Do you want to save file?")
    print("Yes No Cancel Answer:", ans)

tk.Button(app, text="Show Info", command=info_msg).pack(pady=10)
tk.Button(app, text="Show Warning", command=warning_msg).pack(pady=10)
tk.Button(app, text="Show Error", command=error_msg).pack(pady=10)

tk.Button(app, text="Ask Yes/No", command=ask_yes_no).pack(pady=10)
tk.Button(app, text="Ask OK/Cancel", command=ask_ok_cancel).pack(pady=10)
tk.Button(app, text="Ask Retry/Cancel", command=ask_retry_cancel).pack(pady=10)
tk.Button(app, text="Ask Yes/No/Cancel", command=ask_yes_no_cancel).pack(pady=10)

app.mainloop()

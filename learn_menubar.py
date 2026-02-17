import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title("MenuBar Example")
app.geometry("800x400")


def opening_file(event = None):
    messagebox.showinfo("Open File", "You click on Opening File Menu button")

def quit_app(event = None):
    app.quit()

menubar = tk.Menu(app)

file_menu = tk.Menu(menubar, tearoff = 0)
file_menu.add_command(label = 'New', accelerator = 'Ctrl+N')
file_menu.add_command(label = 'Open', accelerator = 'Ctrl+O', command = opening_file)
file_menu.add_command(label = 'Save')
file_menu.add_separator()
file_menu.add_command(label = 'Quit', accelerator = 'ctrl+q', command = quit_app)

menubar.add_cascade(label = 'File', menu = file_menu)



mode_menu = tk.Menu(menubar, tearoff = 0)

mode_menu.add_command(label = "About Me", accelerator = "ctrl+shift+a")
mode_menu.add_command(label = "Check Update")

menubar.add_cascade(label = "Mode", menu = mode_menu)


def dark_light():
    xy = check_var.get()
    
    if xy == 1:
        app.config(bg = "black")
    else:
        app.config(bg = 'white')

check_var = tk.IntVar()

theme = tk.Menu(menubar, tearoff = 0)
theme.add_checkbutton(label = 'Dark', variable = check_var, command = dark_light)



menubar.add_cascade(label = "Theme", menu = theme)



app.config(menu = menubar)


app.bind("<Control-q>", quit_app)
app.bind("<Control-o>", opening_file)

app.mainloop()



# code : https://miro.com/app/board/uXjVG_K0I1w=/?share_link_id=514603268982
import tkinter as tk
import os
from tkinter import filedialog, messagebox

app = tk.Tk()
app.title("Untitled - Notepad")
app.geometry("900x600")

current_font_family = 'Consolas'
current_font_size = 12

text_area = tk.Text(app, undo = True, wrap = 'word', font = (current_font_family, current_font_size))
text_area.pack(fill = 'both', expand = True)

# Scrollbar
scrollbar = tk.Scrollbar(text_area)
scrollbar.pack(fill = 'y', side = 'right')
text_area.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = text_area.yview)

file_path = None

def new_file():
    global file_path
    text_area.delete(1.0, tk.END)
    file_path = None
    app.title("Untitled - Notepad")

def open_file():
    global file_path
    file = filedialog.askopenfilename(defaultextension = '.txt', filetypes = [('Text Files', '*.txt'), ('All Files', "*.*")])

    if file:
        file_path = file
        app.title(os.path.basename(file) + ' - Notepad')
        with open(file, 'r', encoding = 'utf-8') as f:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, f.read())

def save_file():
    global file_path
    if file_path:
        with open(file_path, 'w', encoding = 'utf-8') as f:
            f.write(text_area.get(1.0, tk.END))
    else:
        save_as_file()


def save_as_file():
    global file_path
    file = filedialog.asksaveasfilename(defaultextension = '.txt', filetypes = [('Text Files', '*.txt'), ('All Files', "*.*")])

    if file:
        file_path = file
        app.title(os.path.basename(file) + ' - Notepad')
        with open(file, 'w', encoding = 'utf-8') as f:
            f.write(text_area.get(1.0, tk.END))


def quit_app():
    if messagebox.askokcancel("Exit", "You really want to exit this App"):
        app.quit()


def set_dark_theam():
    text_area.config(bg = "black", fg = "white", insertbackground = "white")

def set_light_theam():
    text_area.config(bg = "white", fg = "black", insertbackground = "black")


def about_me():
    messagebox.showinfo("My Notepad", "This is created as advance Text Editor.For any issue EMial us or Drop an message on 8219836118 this number.")

def update_font():
    text_area.config(font = (current_font_family, current_font_size))

def set_font_family(family):
    global current_font_family
    current_font_family = family
    update_font()

def set_chnage_font(s):
    global current_font_size
    current_font_size = s
    update_font()

# Menus
menu_bar = tk.Menu(app)
app.config(menu = menu_bar)

file_manu = tk.Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = 'File', menu = file_manu)

file_manu.add_command(label = 'New', accelerator = 'Ctrl+N', command = new_file)
file_manu.add_command(label = 'Open', accelerator = 'Ctrl+O', command = open_file)
file_manu.add_command(label = 'Save', accelerator = 'Ctrl+S', command = save_file)
file_manu.add_command(label = 'Save As', command = save_as_file)
file_manu.add_separator()
file_manu.add_command(label = 'Exit', accelerator = 'Ctrl+Q', command = quit_app)

app.bind('<Control-n>', lambda event : new_file())
app.bind('<Control-o>', lambda event : open_file())
app.bind('<Control-s>', lambda event : save_file())
app.bind('<Control-q>', lambda event : quit_app())



edit_manu = tk.Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = 'Edit', menu = edit_manu)

edit_manu.add_command(label = "Undo", command = text_area.edit_undo, accelerator = 'Ctrl+z')
edit_manu.add_command(label = "Redo", command = text_area.edit_redo, accelerator = 'Ctrl+y')
edit_manu.add_separator()
edit_manu.add_command(label = "Cut", command = lambda : text_area.event_generate('<<Cut>>'), accelerator = 'Ctrl+x')
edit_manu.add_command(label = "Copy", command = lambda : text_area.event_generate('<<Copy>>'), accelerator = 'Ctrl+c')
edit_manu.add_command(label = "past", command = lambda : text_area.event_generate('<<Paste>>'), accelerator = 'Ctrl+v')



font_manu = tk.Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = 'Font', menu = font_manu)

font_manu.add_command(label = 'Consolas', command = lambda : set_font_family('consolas'))
font_manu.add_command(label = 'Arial', command = lambda : set_font_family('Arial'))
font_manu.add_command(label = 'Times New Roman', command = lambda : set_font_family('Times New Roman'))
font_manu.add_command(label = 'Courier New', command = lambda : set_font_family('Courier New'))

font_size_menu = tk.Menu(font_manu, tearoff = 0)
font_manu.add_cascade(label = "Font Size", menu = font_size_menu)

for i in range(8, 60, 2):
    font_size_menu.add_command(label = str(i), command = lambda s = i : set_chnage_font(s))


theam_manu = tk.Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = 'Theame', menu = theam_manu)

theam_manu.add_command(label = "Set Dark Mode", command = set_dark_theam)
theam_manu.add_command(label = "Set Light Mode", command = set_light_theam)

about_manu = tk.Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = 'About', menu = about_manu)

about_manu.add_command(label = "About Me", command = about_me)


app.mainloop()


# Notes : https://miro.com/app/board/uXjVG5rhmcU=/?share_link_id=160498503325
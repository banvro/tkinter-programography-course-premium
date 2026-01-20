
import tkinter as tk

app = tk.Tk()

app.geometry('800x400')
app.title("This is first App")
app.config(background = '#43f728')
app.resizable(True, False)
app.iconphoto(True, tk.PhotoImage(file='mylogo.png'))



app.mainloop()
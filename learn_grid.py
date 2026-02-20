
import tkinter as tk

app = tk.Tk()
app.geometry("600x300")
app.title('Learn grid')

app.columnconfigure(0, weight = 1)
app.columnconfigure(1, weight = 2)

app.rowconfigure(1, weight = 2)

tk.Label(app, text = 'x').grid(row = 0, column = 0, sticky = "ew")
tk.Label(app, text = "Password").grid(row = 1, column = 0)

tk.Entry(app).grid(row = 0, column = 1, sticky = "ew", padx = 30)
tk.Entry(app).grid(row = 1, column = 1, pady = 20, padx = 20, sticky = "ew")

tk.Button(app, text = 'Login').grid(row = 2, column = 0, columnspan = 2)




app.mainloop()


#Notes https://miro.com/app/board/uXjVG9-V3sU=/?share_link_id=286661730203
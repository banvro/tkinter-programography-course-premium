import tkinter as tk

root = tk.Tk()
root.geometry("1000x690")
root.title("Learn Frames")
root.config(background = '#58fa55')

frame1 = tk.Frame(root, bg = '#fff763', relief = 'raised', borderwidth = 15)
frame1.pack(fill = 'x')

tk.Label(frame1, text = 'Contact Us Form', font = ('robort', 34, 'bold'), bg = '#fff763').pack(ipady = 25)

frame2 = tk.Frame(root, bg = '#d1d0c5', relief = 'groove', borderwidth = 15)
frame2.pack(fill = 'x')

tk.Label(frame2, text = "" ).grid(row = 0, column = 0, padx = 70, pady = 10)
tk.Label(frame2, text = "Name     :", font = ("robort", 24, "bold"), bg = '#d1d0c5').grid(row = 1, column = 1)
tk.Label(frame2, text = "Age     :", font = ("robort", 24, "bold"), bg = '#d1d0c5').grid(row = 2, column = 1)
tk.Label(frame2, text = "Number  :", font = ("robort", 24, "bold"), bg = '#d1d0c5').grid(row = 3, column = 1)
tk.Label(frame2, text = "Message  :", font = ("robort", 24, "bold"), bg = '#d1d0c5').grid(row = 4, column = 1)

tk.Entry(frame2, font = ("robort", 24)).grid(row = 1, column = 2)
tk.Entry(frame2, font = ("robort", 24)).grid(row = 2, column = 2, pady = 15, padx = 14)
tk.Entry(frame2, font = ("robort", 24)).grid(row = 3, column = 2)
tk.Text(frame2, font = ("robort", 24), width = 20, height = 3).grid(row = 4, column = 2, pady = 15)

tk.Button(frame2, text = "Submit", font = ("robort", 19), bg = 'green').grid(row = 5, column = 2, ipadx = 30)


frame3 = tk.Frame(root, bg = '#58e06c', relief = 'raised', borderwidth = 15)
frame3.pack(fill = 'x')

tk.Label(frame3, text = 'Or Please Contact On Call / Whatsapp', bg = '#58e06c', font = ("robort", 24, 'bold')).pack()
tk.Label(frame3, text = '8219836118', bg = '#58e06c', font = ("robort", 24, 'bold')).pack()


root.mainloop()


# Notes : https://miro.com/app/board/uXjVG7EImQY=/?share_link_id=387366750754
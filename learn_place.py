import tkinter as tk

root = tk.Tk()
root.title("Learn Full place()")
root.geometry("700x400")

# tk.Label(root, text = 'Hellow world').place(x = 300, y =100)
# tk.Button(root, text = "Submit").place(x = 100, y = 300, width = 60, height = 80)
# tk.Button(root, text = "new Submit").place(x = 600, y = 30)



tk.Label(root, text = 'Hellow world').place(relx = 0.5, rely = 0.45)

tk.Button(root, text = "Submit").place(relx = 0.1, rely = 0.2)

tk.Button(root, text = "new Submit", bg = 'red').place(relx = 0.5, rely = 0.5, anchor = 'center', relwidth = 0.3, relheight = 0.3)


root.mainloop()

# Notes : https://miro.com/app/board/uXjVG7pwiYo=/?share_link_id=586335751911
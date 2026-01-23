
import tkinter as tk

root = tk.Tk()
root.geometry('1000x570')
root.title('Add Two Numbers')
root.config(background = '#522bed')

def addingnumbers():
    num1 = int(ent1.get())
    num2 = int(ent2.get())

    sum = num1 + num2
    
    lblshow.config(text = f"The sum of {num1} and {num2} is : {sum}")

    ent1.delete(0, tk.END)
    ent2.delete(0, tk.END)


lbl = tk.Label(root, text = 'Enter Any Two Numbers', font = ('Comic Sans MS', 45, 'bold'), fg = 'white', bg = '#176b02')
lbl.pack(fill = 'x', padx = 30, pady = 30, ipady = 6)

ent1 = tk.Entry(root, font = ('Comic Sans MS', 35, 'bold'), fg = '#176b02')
ent1.pack()

ent2 = tk.Entry(root, font = ('Comic Sans MS', 35, 'bold'), fg = '#176b02')
ent2.pack(pady = 30)

btn = tk.Button(root, text = 'Check Sum', font = ('Comic Sans MS', 23, 'bold'), fg = 'white', bg = '#176b02', command = addingnumbers)
btn.pack(ipadx = 30)

lblshow = tk.Label(root, text = "", fg = 'white', background = '#522bed', font = ('Comic Sans MS', 20, 'bold'))
lblshow.pack(pady = 30)


root.mainloop()
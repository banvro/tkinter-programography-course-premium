
import tkinter as tk
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

app = tk.Tk()
app.geometry('1000x420')
app.title('Age Calculator')
app.config(background = '#29d668')

def check_age():
    dob = ent.get()

    new_date = datetime.strptime(dob, "%d-%m-%Y").date()
    current_date = date.today()
    
    my_age = relativedelta(current_date, new_date)

    lblshow.config(text = f"You are {my_age.years} Years, {my_age.months} Months and {my_age.days} Days Years Old.")
    


lbl1 = tk.Label(app, text = 'Check Your Exact Age', font = ('Comic Sans MS' ,40, 'bold'), fg = 'white', bg = '#068a26')
lbl1.pack(fill = 'x', padx = 30, pady = 20, ipady = 15)

ent = tk.Entry(app, font = ('Arial' ,35), bg = '#dce0dd')
ent.pack()

btn = tk.Button(app, text = 'Check Age', font = ('Arial' ,25, 'bold'), fg = 'white', bg = '#068a26', command = check_age)
btn.pack(pady = 25)

lblshow = tk.Label(app, text = '', font = ('Arial' ,25), fg = '#068a26', bg = '#29d668')
lblshow.pack()

app.mainloop()
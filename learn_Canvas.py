import tkinter as tk
from PIL import Image, ImageTk

app = tk.Tk()
app.geometry('1000x700')
app.title('Learn Canvas')
app.config(background = '#29d668')

canvas = tk.Canvas(app, width = 700, height = 600, bg = "white", relief = "raised", bd = 10)
canvas.pack()

canvas.create_line(10, 10, 500, 500, fill = "red", width = 5, 
        dash = (5, 2), arrow = "both", arrowshape = (10, 15, 15)
)

canvas.create_rectangle(50, 50, 400, 400, fill = "red", dash = (5, 3), width = 3, outline = "green",
            activefill = "green", activeoutline = "red"

)

canvas.create_oval(100, 100, 600, 600, fill = "gray")
canvas.create_arc(100, 100, 600, 600, start = 0, extent = 30, fill = "green")

canvas.create_polygon(100, 200, 150, 300, 50, 300)

canvas.create_text(400, 400, text = "hwllow wolrd", font=("Arial", 16, "bold"), fill = "green",
        activefill = "red"
)

img = Image.open("1.jpg")
new_img = ImageTk.PhotoImage(img)

canvas.create_image(100, 100, image = new_img)




app.mainloop()



# Notes : https://miro.com/app/board/uXjVG2U2uSY=/?share_link_id=469530559122
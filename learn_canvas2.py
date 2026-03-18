import tkinter as tk

root = tk.Tk()
root.title("Advance Canvas")

canvas = tk.Canvas(root, width = 900, height = 600, bg = "white")
canvas.pack()

def show_cordinas(event):
    print(f"X : {event.x} and Y : {event.y}")

canvas.bind('<Button-3>', show_cordinas)


react = canvas.create_rectangle(50, 150, 200, 300, fill = "red")

oval = canvas.create_oval(250, 150, 400, 300, fill = "green")

def color_chnage():
    # canvas.delete(react)
    # canvas.create_oval(50, 150, 200, 300, fill = "red")
    canvas.itemconfig(react, fill = "yellow")

btn = tk.Button(root, text = "Chnage React color", command = color_chnage)

canvas.create_window(763, 29, window = btn)

current_item = None 
last_x, last_y = 0, 0

def on_click(event):
    global current_item, last_x, last_y
    items = canvas.find_closest(event.x, event.y)
    if items:
        current_item = items[0]
        last_x, last_y = event.x, event.y

def on_drag(event):
    global last_x, last_y
    if current_item:
        dx = event.x - last_x
        dy = event.y - last_y

        canvas.move(current_item, dx, dy)
        last_x, last_y = event.x, event.y


canvas.bind('<Button-1>', on_click)
canvas.bind('<B1-Motion>', on_drag)



ball = canvas.create_oval(10, 500, 50, 540, fill = "blue")

def moving_ball():
    canvas.move(ball, 5, 0)
    pos = canvas.coords(ball)

    if pos[2] > 900:
        canvas.coords(ball, 10, 500, 50, 540)

    root.after(10, moving_ball)

moving_ball()

root.mainloop()


# notes : https://miro.com/app/board/uXjVGvjS7tE=/?share_link_id=296273148565
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Learn - Tkinter Image")
root.geometry("800x700")

img = Image.open("img2.jpg")
# img = img.resize((700, 400))
img = img.rotate(30)
img = img.convert("1")

tk_img = ImageTk.PhotoImage(img)

tk.Label(
    root, text = "Nature Image", image = tk_img, 
    font = ("robot", 30, "bold"), fg = "red",
    compound = "top", bg = "white", 
    relief = "ridge", bd = 14,
    ).pack(ipadx = 20, ipady = 20)


img2 = Image.open("img1.jpg")
img2 = img2.resize((150, 60))
img2_tk = ImageTk.PhotoImage(img2)

tk.Button(root, text = "Submit", image = img2_tk, compound = "center", font = ("robot", 10, "bold"), fg = "red",).pack(pady = 40)




root.mainloop()
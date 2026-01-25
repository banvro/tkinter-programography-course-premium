import tkinter as tk

# ---------------- WINDOW ----------------
app = tk.Tk()
app.title("Tkinter Space Management Demo")
app.geometry("700x450")
app.config(bg="#dddddd")


# ---------------- HEADER (fill X) ----------------
header = tk.Label(
    app,
    text="Spacing in Tkinter",
    font=("Arial", 26, "bold"),
    bg="#2c7be5",
    fg="white",
    pady=15,           # INNER padding
)
header.pack(fill="x")  # Fills horizontal space


# ---------------- MAIN FRAME ----------------
main_frame = tk.Frame(
    app,
    bg="#f5f5f5",
    padx=20,           # INNER padding of frame
    pady=20
)
main_frame.pack(
    fill="both",
    expand=True,
    padx=20,           # OUTER padding (margin)
    pady=20
)


# ---------------- LEFT PANEL ----------------
left_frame = tk.Frame(
    main_frame,
    bg="#ffffff",
    bd=2,
    relief="groove",
    padx=15,
    pady=15
)
left_frame.pack(
    side="left",
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

tk.Label(
    left_frame,
    text="Left Panel",
    font=("Arial", 18, "bold"),
    anchor="w"          # Text aligned inside widget
).pack(fill="x", pady=(0, 10))

tk.Button(
    left_frame,
    text="Button 1",
    padx=20,            # INNER padding
    pady=10
).pack(pady=5)

tk.Button(
    left_frame,
    text="Button 2",
    width=15,           # TEXT units
    height=2
).pack(pady=5)


# ---------------- RIGHT PANEL ----------------
right_frame = tk.Frame(
    main_frame,
    bg="#ffffff",
    bd=2,
    relief="groove",
    padx=15,
    pady=15
)
right_frame.pack(
    side="right",
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

tk.Label(
    right_frame,
    text="Right Panel",
    font=("Arial", 18, "bold"),
    anchor="w"
).pack(fill="x", pady=(0, 10))

entry = tk.Entry(
    right_frame,
    font=("Arial", 16),
    bd=4,
    relief="sunken",
    highlightthickness=2,
    highlightcolor="blue",
    highlightbackground="gray"
)
entry.pack(fill="x", padx=10, pady=10)
entry.insert(0, "Text inside Entry")  # Pre-filled text


tk.Button(
    right_frame,
    text="Submit",
    padx=25,
    pady=10,
    bg="#28a745",
    fg="white"
).pack(pady=20)


# ---------------- FOOTER ----------------
footer = tk.Label(
    app,
    text="Footer uses pady + fill",
    bg="#333333",
    fg="white",
    pady=10
)
footer.pack(fill="x")


app.mainloop()

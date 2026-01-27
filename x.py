import tkinter as tk

root = tk.Tk()
root.title("Checkbutton – All Options Demo")
root.geometry("520x420")
root.config(bg="lightgray")

# control variables
cb1_var = tk.IntVar(value=1)
cb2_var = tk.StringVar(value="OFF")
cb3_var = tk.StringVar(value="MAYBE")

def checked():
    print("Checkbutton values:")
    print("CB1:", cb1_var.get())
    print("CB2:", cb2_var.get())
    print("CB3:", cb3_var.get())
    print("-" * 30)

cb1 = tk.Radiobutton(
    root,

    # --- TEXT / DISPLAY ---
    text="Enable Feature A",
    font=("Arial", 12, "bold"),      # font style
    fg="blue",                       # text color
    bg="lightgray",                  # background color
    activeforeground="red",          # text color on hover
    activebackground="yellow",       # background on hover
    disabledforeground="gray",       # text color when disabled
    justify="left",                  # text alignment
    wraplength=200,                  # wrap text after width
    underline=0,                     # underline character index

    # --- VARIABLE / VALUE ---
    variable=cb1_var,                # control variable
    # onvalue=1,                       # value when checked
    # offvalue=0,                      # value when unchecked

    # --- INDICATOR / STYLE ---
    indicatoron=True,                # True = checkbox, False = button style
    selectcolor="green",             # color when checked
    width=25,                        # widget width
    height=2,                        # widget height
    padx=10,                         # internal x padding
    pady=5,                          # internal y padding
    relief="groove",                 # border style
    borderwidth=3,                   # border thickness

    # --- HIGHLIGHT ---
    highlightthickness=2,            # focus border thickness
    highlightbackground="black",     # focus border (inactive)
    highlightcolor="red",             # focus border (active)

    # --- STATE / INTERACTION ---
    state="normal",                  # normal / disabled
    command=checked,                 # function on toggle
    cursor="hand2",                  # mouse cursor
    takefocus=True,                  # allow keyboard focus

    # --- LAYOUT ---
    anchor="w"                       # alignment inside widget
)

cb2 = tk.Checkbutton(
    root,
    text="Dark Mode",
    bg="lightgray",
    variable=cb2_var,
    onvalue="ON",
    offvalue="OFF",
    command=checked
)

cb3 = tk.Checkbutton(
    root,
    text="Experimental Option (Tri-state)",
    bg="lightgray",
    variable=cb3_var,
    onvalue="YES",
    offvalue="NO",
    tristatevalue="MAYBE",            # third state
    command=checked
)

cb1.pack(pady=10, anchor="w")
cb2.pack(pady=10, anchor="w")
cb3.pack(pady=10, anchor="w")

root.mainloop()

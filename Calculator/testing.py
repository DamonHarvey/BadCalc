import tkinter as tk

root = tk.Tk()
root.title("Button Box Example")


# 1. Create the 'Box' (LabelFrame)
button_box = tk.Frame(root)
button_box.grid(column=0, row=1, columnspan=2, rowspan=2)

# 2. Add buttons inside the 'Box'
btn1 = tk.Button(button_box, text="Action 1", command=lambda: print("Button 1 clicked"))
btn1.grid(column=0, row=0)

btn2 = tk.Button(button_box, text="Action 2", command=lambda: print("Button 2 clicked"))
btn2.grid(column=1, row=1)


button3 = tk.Button(root, text="Action 2", command=lambda: print("Button 2 clicked"))
button3.grid(column=0, row=0, sticky="W")

root.mainloop()

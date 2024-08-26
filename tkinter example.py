import tkinter as tk

root = tk.Tk()
root.title("Tkinter World")

label = tk.Label(root, text="Welcome")  # Corrected 'label' to 'Label'
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Click Me!!")
button.pack()

root.mainloop()

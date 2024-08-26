import tkinter as tk

win = tk.Tk()

frame1 = tk.Frame(master=win, width=100, height=100, bg='orange')
frame1.pack()

frame2 = tk.Frame(master=win, width=50, height=50, bg='blue')
frame2.pack()

frame1 = tk.Frame(master=win, width=25, height=25, bg='green')
frame1.pack()

win.mainloop()
import tkinter as tk

win = tk.Tk()

frame1 = tk.Frame(master=win, height=80, bg='red')
frame1.pack(fill=tk.X)

frame2 = tk.Frame(master=win, height=50, bg='yellow')
frame2.pack(fill=tk.X)

frame3 = tk.Frame(master=win, height=40, bg='blue')
frame3.pack(fill=tk.X)

win.mainloop()
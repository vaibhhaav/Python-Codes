import tkinter as tk
from tkinter import messagebox

def validate_login():
    userid = username_entry.get()
    password = password_entry.get()
    
    if userid == "admin" and password == "password":
        messagebox.showinfo("Login Successful","Welcome, Admin")
    else:
        messagebox.showerror("Login Failed","Invalid username or Password")


p = tk.Tk()
p.title("Login Form")

username_label = tk.Label(p,text="Userid: ")
username_label.pack()

username_entry = tk.Entry(p)
username_entry.pack()

password_label = tk.Label(p,text="Password: ")
password_label.pack()

password_entry = tk.Entry(p,show="*")
password_entry.pack()

login_button = tk.Button(p,text="Login",command=validate_login)
login_button.pack()

p.mainloop()
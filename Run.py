from login import LoginBody
from tkinter import messagebox

if __name__ == '__main__':
    try:
        LoginBody()
    except Exception as e:
        messagebox.showerror('错误', e)







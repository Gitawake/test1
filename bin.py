from tkinter import *
from tkinter import messagebox
from requests_html import HTMLSession

from Box import *

app = Tk()
app.title('爬虫训练系统v1.0.0')
app.geometry('800x500')
monty = LabelFrame(app, text='login')
monty.pack(side='top', expand='yes')

Label(monty, text='手机号码:').grid(row=0)
Label(monty, text='验证码:').grid(row=1)
phone = Entry(monty, validate="focusout")
vcode = Entry(monty, validate="focusout")
phone.grid(row=0, column=1, padx=10, pady=5)
vcode.grid(row=1, column=1, padx=10, pady=5)

session = HTMLSession()
r = session.get('https://www.cnblogs.com/shapeL/p/9037035.html')

r.html.xpath()
print()

def show():
    nuberyz(phone.get(), vcode.get())
    phone.delete(0, END)
    vcode.delete(0, END)


Button(monty, text="验证", width=10, command=show).grid(row=3, column=0, sticky=W, padx=10, pady=5)
Button(monty, text="退出", width=10, command=app.destroy).grid(row=3, column=1, sticky=E, padx=10, pady=5)

app.mainloop()

from tkinter import *


class MainBody(object):

    def homepage(self, app):
        monty = LabelFrame(app, text='loginxxx')
        monty.pack(side='top', expand='yes')
        Label(monty, text='手机号码:').grid(row=0)
        Label(monty, text='验证码:').grid(row=1)
        phone = Entry(monty, validate="focusout")
        vcode = Entry(monty, validate="focusout")
        phone.grid(row=0, column=1, padx=10, pady=5)
        vcode.grid(row=1, column=1, padx=10, pady=5)

        def show():
            print('验证通过了')

        Button(monty, text="验证", width=10, command=show).grid(row=3, column=0, sticky=W, padx=10, pady=5)
        Button(monty, text="退出", width=10, command=app.destroy).grid(row=3, column=1, sticky=E, padx=10, pady=5)

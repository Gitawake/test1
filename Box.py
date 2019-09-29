from tkinter import messagebox
from tkinter import *


class LoginBody(object):
    Window_title = '爬虫训练系统v1.0.0'
    Window_size = '800x500'

    zcode = str(456456)
    xnuber = str(13713777056)

    @staticmethod
    def login_ui(app):
        monty = LabelFrame(app, text='login')
        monty.pack(side='top', expand='yes')

        Label(monty, text='手机号码:').grid(row=0)
        Label(monty, text='验证码:').grid(row=1)
        phone = Entry(monty, validate="focusout")
        vcode = Entry(monty, validate="focusout")
        phone.grid(row=0, column=1, padx=10, pady=5)
        vcode.grid(row=1, column=1, padx=10, pady=5)

        def show():
            if LoginBody.login_verification(phone.get(), vcode.get()):
                app.update()
                LoginBody.Window_size = str(app.winfo_width()) + 'x' + str(app.winfo_height())
                monty.destroy()
                MainBody.homepage(app)
            else:
                phone.delete(0, END)
                vcode.delete(0, END)

        Button(monty, text="验证", width=10, command=show).grid(row=3, column=0, sticky=W, padx=10, pady=5)
        Button(monty, text="退出", width=10, command=app.destroy).grid(row=3, column=1, sticky=E, padx=10, pady=5)

    @staticmethod
    def login_verification(nuber, code):
        try:
            if re.match(r'^1[0-9]\d{9}$', nuber):
                if re.match(r'\d{6}$', code):
                    if code == LoginBody.zcode and nuber == LoginBody.xnuber:
                        # print('验证通过')
                        return True
                    else:
                        messagebox.showerror('错误', '验证失败')

                else:
                    # print('输入的验证码格式错误')
                    messagebox.showerror('错误', '输入的验证码格式错误')
            else:
                # print('输入的手机号码格式错误')
                messagebox.showerror('错误', '输入的手机号码格式错误')
        except Exception as e:
            # print(e)
            messagebox.showerror('错误', e)


class MainBody(object):

    @staticmethod
    def homepage(app):

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

from tkinter import *
from tkinter import messagebox
from home import MainBody


class LoginBody(object):

    def __init__(self):

        self.Window_title = '爬虫训练系统v1.0.0'
        self.Window_size = '800x500'

        self.zcode = str(456456)
        self.xnuber = str(13713777056)

        self.monty = None
        self.phone = None
        self.vcode = None

        self.app = Tk()
        self.app.title(self.Window_title)
        self.app.geometry(self.Window_size)
        self.login_ui()
        self.app.mainloop()

    def login_ui(self):
        try:
            self.monty = LabelFrame(self.app, text='login')
            self.monty.pack(side='top', expand='yes')

            Label(self.monty, text='手机号码:').grid(row=0)
            Label(self.monty, text='验证码:').grid(row=1)
            self.phone = Entry(self.monty, validate="focusout")
            self.vcode = Entry(self.monty, validate="focusout")
            self.phone.grid(row=0, column=1, padx=10, pady=5)
            self.vcode.grid(row=1, column=1, padx=10, pady=5)

            Button(self.monty, text="验证", width=10, command=self.entry_verification).grid(row=3, column=0, sticky=W, padx=10, pady=5)
            Button(self.monty, text="退出", width=10, command=self.app.destroy).grid(row=3, column=1, sticky=E, padx=10, pady=5)
        except Exception as e:
            messagebox.showerror('错误', e)

    def entry_verification(self):
        try:
            if self.login_verification(self.phone.get(), self.vcode.get()):
                self.app.update()
                self.Window_size = str(self.app.winfo_width()) + 'x' + str(self.app.winfo_height())
                self.monty.destroy()
                MainBody().homepage(self.app)
            else:
                self.phone.delete(0, END)
                self.vcode.delete(0, END)
        except Exception as e:
            messagebox.showerror('错误', e)

    def login_verification(self, number, code):
        try:
            if re.match(r'^1[0-9]\d{9}$', number):
                if re.match(r'\d{6}$', code):
                    if code == self.zcode and number == self.xnuber:
                        return True
                    else:
                        messagebox.showerror('错误', '验证失败')
                else:
                    messagebox.showerror('错误', '输入的验证码格式错误')
            else:
                messagebox.showerror('错误', '输入的手机号码格式错误')
        except Exception as e:
            messagebox.showerror('错误', e)



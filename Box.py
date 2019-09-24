import re
from tkinter import messagebox


def nuberyz(xnuber, xcode):
    zcode = str(456456)
    nuber = xnuber
    try:
        if re.match(r'^1[0-9]\d{9}$', nuber):
            code = xcode
            if re.match(r'\d{6}$', code):
                if code == zcode:
                    # print('验证通过')
                    messagebox.showinfo('消息', '验证通过')
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

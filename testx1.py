import random
import re
import time
import sys
import win32ui
import tkinter
import calendar
import os

# 循环倒计时打印
# i = range(1, 6)
# for i in reversed(i):
#     print(i)
#     sys.stdout.flush()
#     time.sleep(1)


# 两个数求和
# kk = input('请输入kk的数值：')
# ll = input('请输入ll的数值：')

# sum = float(kk)+float(ll)
#
# print('{0} + {1} = {2}' .format(kk, ll, sum))


# 数值的平方根
# num = float(input())
#
# num_ds = num ** 0.5
#
# print('%0.3f 的平方根是 %0.3f' % (num, num_ds))


# 随机数
# print(random.randint(0, 9))

# 变量交换
# x = input('请输入x的值：')
# y = input('请输入y的值：')
#
# x, y = y, x
# print('交换后：x={0},y={1}'.format(x, y))

# if语句
# num = float(input('请输入一个数值：'))
# if num > 0:
#     print('正数')
# elif num == 0:
#     print('为零')
# else:
#     print('负数')

# if语句内嵌
# num = float(input('请输入一个数值：'))
# if num >= 0:
#     if num > 0:
#         print('正数')
#     else:
#         print('为零')
# else:
#     print('负数')

# 判断期数偶数
# num = int(input('请输入一个数字：'))
# if (num % 2) == 0:
#     print('{0}是偶数'.format(num))
# else:
#     print('{0}是奇数'.format(num))

# 判断闰年
# year = int(input("输入一个年份: "))
# print(year % 4)
# print(year % 100)
# print(year % 400)
# if (year % 4) == 0:
#    if (year % 100) == 0:
#        if (year % 400) == 0:
#            print("{0} 是闰年".format(year))   # 整百年能被400整除的是闰年
#        else:
#            print("{0} 不是闰年".format(year))
#    else:
#        print("{0} 是闰年".format(year))       # 非整百年能被4整除的为闰年
# else:
#    print("{0} 不是闰年".format(year))

# 取最大值
# print(max(1, 5, 9))
# print(max([4, 19, 8]))

# 九九乘法表
# for j in range(1, 10):
#     for i in range(1, j+1):
#         print('{0}x{1}={2}\t'.format(i, j, j*i), end='')
#     print()

# 日历
# yy = int(input('请输入年份：'))
# mm = int(input('请输入月份：'))
#
# print(calendar.month(yy, mm))

# 文件操作
# with open('test.txt', 'wt')as out_file:
#     out_file.write('hshshshshssh')
#
# with open('test.txt', 'rt')as in_file:
#     text = in_file.read()
# print(text)

# 判断字符串
# str = "555566ss"
# print(str.isdigit())
from tkinter import messagebox

# 正则表达
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





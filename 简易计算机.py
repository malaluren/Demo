import tkinter as tk



# 功能
# 追加数字
def add_num(n):
    if lists[0] == '0':
        lists[0] = n
        result_num.set(''.join(lists))
    else:
        lists.append(n)
        result_num.set(''.join(lists))


# 选择运算符号
def operator(i):
    if len(lists) > 0:
        if lists[-1] in ['+', '-', '*', '/']:
            lists[-1] = i
        else:
            lists.append(i)
    result_num.set(''.join(lists))


# 清零
def clear():
    lists.clear()
    lists.append('0')
    result_num.set('0')


# 后退
def back():
    if len(lists) > 1:
        del lists[-1]
        result_num.set(''.join(lists))
    else:
        pass


# 计算
def equal():
    a = ''.join(lists)
    end_num = eval(a)
    result_num.set(end_num)
    lists.clear()
    lists.append(str(end_num))


# 界面
# 实例化窗口
root = tk.Tk()
# 标题
root.title('计算机')
# 窗口大小，位置
root.geometry("295x280+500+200")
# 透明度和颜色
root.attributes("-alpha", 0.9)
root['background'] = '#f5f5f7'

lists = ['0']
result_num = tk.StringVar()
result_num.set('0')

# 标签
label1 = tk.Label(root, textvariable=result_num, width=20, height=2, font=('宋体', 20), background='#f5f5f7', justify='left',
                  anchor='se')
# 布局
label1.grid(row=0, column=0, columnspan=4)


# 按钮
class button():
    button_clear = tk.Button(root, text="C", width=4, font=('宋体', 16), background='#C0C0C0', command=lambda: clear())
    button_clear.grid(padx=4, row=1, column=0)

    button_Division = tk.Button(root, text="/", width=4, font=('宋体', 16), background='#C0C0C0', command=lambda: operator('/'))
    button_Division.grid(padx=4, row=1, column=1)

    button_Multiplication = tk.Button(root, text="*", width=4, font=('宋体', 16), background='#C0C0C0', command=lambda: operator('*'))
    button_Multiplication.grid(padx=4, row=1, column=2)

    button_back = tk.Button(root, text="←", width=4, font=('宋体', 16), background='#C0C0C0', command=lambda: back())
    button_back.grid(padx=4, row=1, column=3)

    button_Seven = tk.Button(root, text="7", width=4, font=('宋体', 16), background='#C0C0C0', command=lambda: add_num('7'))
    button_Seven.grid(padx=4, row=2, column=0)

    button_Eight = tk.Button(root, text="8", width=4, font=('宋体', 16), background='#C0C0C0', command=lambda: add_num('8'))
    button_Eight.grid(padx=4, row=2, column=1)

    button_Nine = tk.Button(root, text="9", width=4, font=('宋体', 16), background='#C0C0C0', command=lambda: add_num('9'))
    button_Nine.grid(padx=4, row=2, column=2)

    button_Subtraction = tk.Button(root, text="-", width=4, font=('宋体', 16), background='#C0C0C0', command=lambda: operator('-'))
    button_Subtraction.grid(padx=4, row=2, column=3)

    button_Four = tk.Button(root, text="4", width=4, font=('宋体', 16), background='#C0C0C0', command=lambda: add_num('4'))
    button_Four.grid(padx=4, row=3, column=0)

    button_Five = tk.Button(root, text="5", width=4, font=('宋体', 16), background='#C0C0C0', command=lambda: add_num('5'))
    button_Five.grid(padx=4, row=3, column=1)

    button_Six = tk.Button(root, text="6", width=4, font=('宋体', 16), background='#C0C0C0', command=lambda: add_num('6'))
    button_Six.grid(padx=4, row=3, column=2)

    button_Addition = tk.Button(root, text="+", width=4, font=('宋体', 16), background='#C0C0C0', command=lambda: operator('+'))
    button_Addition.grid(padx=4, row=3, column=3)

    button_onw = tk.Button(root, text="1", width=4, font=('宋体', 16), background='#C0C0C0', command=lambda: add_num('1'))
    button_onw.grid(padx=4, row=4, column=0)

    button_two = tk.Button(root, text="2", width=4, font=('宋体', 16), background='#C0C0C0', command=lambda: add_num('2'))
    button_two.grid(padx=4, row=4, column=1)

    button_Three = tk.Button(root, text="3", width=4, font=('宋体', 16), background='#C0C0C0', command=lambda: add_num('3'))
    button_Three.grid(padx=4, row=4, column=2)

    button_equal = tk.Button(root, text="=", width=4, height=3, font=('宋体', 16), background='#C0C0C0', command=lambda: equal())
    button_equal.grid(padx=4, row=4, column=3, rowspan=5)

    button_zero = tk.Button(root, text="0", width=10, font=('宋体', 18), background='#C0C0C0', command=lambda: add_num('0'))
    button_zero.grid(padx=4, pady=4, row=5, column=0, columnspan=2)

    button_Point = tk.Button(root, text=".", width=4, font=('宋体', 16), background='#C0C0C0', command=lambda: add_num('.'))
    button_Point.grid(padx=4, row=5, column=2)


button()
print(result_num)

# 消息循环
root.mainloop()

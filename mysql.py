# -*- coding=UTF-8 -*-
import pymysql
from mysql_function import *
import time
import tkinter
from tkinter import ttk
from tkinter import *

db_name = 'super'

def button_search1(event):
    link = show_input.get()
    token = ssrlink_input(link)
    var.set(token)
    user = search_info(db_name, token, table="`link`", table_field="token")
    if user == ():
        var.set("没有找到Token！！！")
        var2.set("没有找到Email！！！")
        x = tree.get_children()
        for item in x:
            tree.delete(item)
    else:
        x = tree.get_children()
        for item in x:
            tree.delete(item)
        j = 0
        for info in user:
            get_user = search_info(
                db_name, info[6], table="`user`", table_field="id")
            tree.insert("", 0, text=j+1,
                        value=(get_user[j][0], get_user[j][2]),)
            var2.set(get_user[j][2])
            j += 1

def button_search2(event):
    get_user = search_FLG(db_name)
    x = tree.get_children()
    for item in x:
        tree.delete(item)
    j = len(get_user) - 1
    i = 1
    while j >= 0:
        tree.insert("", 0, text=i, value=(
            get_user[j][0], get_user[j][1], get_user[j][2]))
        j -= 1
        i += 1

def button_search3(event):
    get_user = search_BT(db_name)
    x = tree.get_children()
    for item in x:
        tree.delete(item)
    j = len(get_user) - 1
    i = 1
    while j >= 0:
        tree.insert("", 0, text=i, value=(
            get_user[j][0], get_user[j][1], get_user[j][2]))
        j -= 1
        i += 1

def button_copy(event):
    user_token = show_output.get()
    window.clipboard_clear()
    window.clipboard_append(user_token)

def button_copy2(event):
    user_email = show_output2.get()
    window.clipboard_clear()
    window.clipboard_append(user_email)

window = tkinter.Tk()
# window.title = "Super用户管理系统"
window.geometry("600x450")

# Treeview显示框
tree = ttk.Treeview(window)
tree["columns"] = ("ID", "Email", "Num")
tree.column("ID", width=100)
tree.column("Email", width=200)
tree.column("Num", width=100)
tree.heading("ID", text="ID")
tree.heading("Email", text="Email")
tree.heading("Num", text="Num")
tree.pack()
# 输入部分组合框
show1_frame = Frame(window)
show1_frame.pack(side="top", pady="5m", anchor="w")

input_lable1 = Label(show1_frame, text="请输入订阅链接:")
show_input = Entry(show1_frame, width=50, relief=SOLID, highlightcolor="grey")
input_lable1.pack(side="left", padx="1m")
show_input.pack(side="left", padx="1m")
# 输出部分组合框
show2_frame = Frame(window)
show2_frame.pack(side="top", pady="5m", anchor="w")

input_lable2 = Label(show2_frame, text="用户订阅链接码:")
var = StringVar()
show_output = Entry(show2_frame, width=40, relief=SOLID,
                    highlightcolor="grey", textvariable=var, state="readonly", fg="red")
var.set("用户Token将在这里显示...")
input_lable2.pack(side="left", padx="1m")
show_output.pack(side="left", padx="1m")

button5 = tkinter.Button(show2_frame, text="点击复制", width=10,
                         activeforeground="pink", activebackground="blue")
button5.bind("<Button-1>", button_copy)
button5.pack(side="left", padx="1m")

# 输出部分组合框2
show3_frame = Frame(window)
show3_frame.pack(side="top", pady="5m", anchor="w")

input_lable3 = Label(show3_frame, text="获取到用户邮箱:")
var2 = StringVar()
show_output2 = Entry(show3_frame, width=40, relief=SOLID,
                     highlightcolor="grey", textvariable=var2, state="readonly", fg="blue")
var2.set("用户Email将在这里显示...")
input_lable3.pack(side="left", padx="1m")
show_output2.pack(side="left", padx="1m")

button6 = tkinter.Button(show3_frame, text="点击复制", width=10,
                         activeforeground="pink", activebackground="blue")
button6.bind("<Button-1>", button_copy2)
button6.pack(side="left", padx="1m")

# 按键部分组合框
button_show = Frame(window)
button_show.pack(side="top", pady="5m")

button1 = tkinter.Button(button_show, text="查询订阅链接", width=10,
                         activeforeground="pink", activebackground="blue")
button1.bind("<Button-1>", button_search1)
button1.pack(side="left", anchor="center")

button2 = tkinter.Button(button_show, text="查询轮子用户", width=10,
                         activeforeground="pink", activebackground="blue")
button2.bind("<Button-1>", button_search2)
button2.pack(side="left", anchor="center")

button3 = tkinter.Button(button_show, text="查询BT用户", width=10,
                         activeforeground="pink", activebackground="blue")
button3.bind("<Button-1>", button_search3)
button3.pack(side="left", anchor="center")

button4 = tkinter.Button(button_show, text="复制用户邮箱", width=10,
                         activeforeground="pink", activebackground="blue")
button4.bind("<Button-1>", button_copy)
# button4.pack(side = "left",anchor = "center")

window.mainloop()

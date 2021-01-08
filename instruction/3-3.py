import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('日程管理')
window.geometry("400x300")

#分页
nb = ttk.Notebook(window,width=380,height=260)
nb.grid(row=0,column=0)
tab1 = tk.Frame(nb)
nb.add(tab1,text = "显示待办")
tab2 = tk.Frame(nb)
nb.add(tab2, text = "管理待办")

#待办名称输入框
l1 = tk.Label(tab2,text="待办名称：")
l1.grid(row=0,column=0)
e1 = tk.Entry(tab2)#可以用get()方法获取输入的内容
e1.grid(row=0,column=1)
#详细信息输入框
l2 = tk.Label(tab2,text="详细信息：")
l2.grid(row=1,column=0)
e2 = tk.Entry(tab2)
e2.grid(row=1,column=1)
#ddl输入框
l6 = tk.Label(tab2,text="ddl:")
l6.grid(row=2,column=0)
e3 = tk.Entry(tab2)
e3.grid(row=2,column=1)
#按钮，可以绑定功能
b1 = tk.Button(tab2,width=40,text="添加待办")#未绑定的按钮
b1.grid(row=3,column=0,columnspan = 2)

window.mainloop()
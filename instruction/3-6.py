#导入库
import tkinter as tk
from tkinter import ttk
import json


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


#载入json数据
def read_data():
    global data #声明全局变量
    with open("data.json","r") as f: #打开本地文件
        data = json.load(f)
read_data()

scrollBar = tk.Scrollbar(tab1) #初始化一个滚动条

#初始化一个treeview表格
columns = ("row", "data", "ddl","time")
tree = ttk.Treeview(tab1, show = "headings", columns = columns, yscrollcommand=scrollBar.set)
tree.column("row", anchor = "center",width = 40)
tree.column("data", anchor = "center",width = 150)
tree.column("ddl", anchor = "center",width = 80)
tree.column("time", anchor = "center",width = 80)
tree.heading("row", text = "编号")
tree.heading("data", text = "待办事项")
tree.heading("ddl", text = "ddl")
tree.heading("time", text = "插入时间")


scrollBar.config(command=tree.yview) #把滚动条绑定到表格
scrollBar.pack(side=tk.RIGHT,fill = tk.Y) #把滚动条显示到窗口中
    
#给treeview表格添加数据
i=0
for data1 in data: #这是一个遍历
    #从data这个数据字典中取数据
    name1 = data[data1]["name"]
    ddl1 = data[data1]["ddl"]
    state1 = data[data1]["state"] #或许该数据的状态，是否显示在表格中，删除数据时的功能
    time1 = data[data1]["time"]
    if state1 == True: #判断是否应该显示在表格中，是删除数据时的功能，先放在这里
        tree.insert("",i,values = (i+1,name1,ddl1,time1))
    i+=1
tree.pack()

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




#存储数据
def get_data():
    datas ={}
    datas["name"] = e1.get()
    datas["details"] = e2.get()
    datas["ddl"] = date.get()
    datas["state"] = True
    datas["time"] = time.strftime("%Y-%m-%d",time.gmtime())

    i=len(data)
    

    
    data[str(i)] = datas
    with open("data.json","w") as f: #打开本地文件
        json.dump(data,f)

#按钮，可以绑定功能
b1 = tk.Button(tab2,width=40,text="添加待办",command=get_data)
b1.grid(row=3,column=0,columnspan = 2)
#print(data) #optional
window.mainloop()

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('日程管理')
window.geometry("400x300")


nb = ttk.Notebook(window,width=380,height=260)
nb.grid(row=0,column=0)
tab1 = tk.Frame(nb)
nb.add(tab1,text = "显示待办")
tab2 = tk.Frame(nb)
nb.add(tab2, text = "管理待办")


window.mainloop()
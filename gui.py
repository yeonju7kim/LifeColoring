import requests as requests
import json
import tkinter as tk

def Doing_what():
    master = tk.Tk()
    master.title('')

    listbox = tk.Listbox(master, selectmode='extended', height=0)
    listbox.insert(1, "수업관련")
    listbox.insert(0, "논문읽기")
    listbox.insert(2, "프로젝트")
    listbox.insert(3, "휴식")

    listbox.pack()
    listbox.select_set(0)
    listbox.grid(row=0,column=0,rowspan=2)
    def handler(e):
        master.quit()
    master.bind('<Return>', handler)#lambda x: master.quit)

    e1 = tk.Entry(master)
    e1.icursor(1)
    e1.grid(row=3,column=0)

    tk.Button(master,text='OK',command=master.quit).grid(row=3,column=1,sticky=tk.W,pady=4)

    master.mainloop()
    task = e1.get()
    category = listbox.selection_get()
    try:
        master.destroy()
        return task, category
    except:
        return task, category

def ok_no_msgbox(question):
    master = tk.Tk()
    master.title('')
    tk.Label(master, text=question).grid(row=0)
    def yes():
        master.quit()
    def no():
        master.quit()
        master.destroy()
    def handler(e):
        master.quit()
    master.bind('<Return>', handler)
    tk.Button(master, text='OK', command=yes).grid(row=1, column=0, sticky=tk.W, pady=4)
    tk.Button(master, text='NO', command=no).grid(row=1, column=1, sticky=tk.W, pady=4)
    master.mainloop()
    try:
        master.destroy()
        return True
    except:
        return False
from tkinter import *
import SelectFiles
import OpenProcess



root = Tk()
root.title('选择模式')
root.geometry("200x100")



def updata():
    if v.get()==1:
        OpenProcess.openBa()
        OpenProcess.webopen()
    elif v.get()==2:
        SelectFiles.selectfiles()
    elif v.get() == 3:
        SelectFiles.appendpath()
    elif v.get() == 4:
        OpenProcess.webselect()

v = IntVar() # 使那个variable不变
a = Radiobutton(root, text='1启动程序', variable=v, value=1,command=updata ).pack()
b = Radiobutton(root, text='2选择程序', variable=v, value=2,command=updata  ).pack()
c = Radiobutton(root, text='3追加程序', variable=v, value=3,command=updata  ).pack()
c = Radiobutton(root, text='4设置网址', variable=v, value=4,command=updata  ).pack()
mainloop()



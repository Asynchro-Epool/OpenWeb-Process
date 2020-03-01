import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
# 调入 tk里tkinter的filedialog

# 选择文件
def selectfiles():
    root = tk.Tk()
    root.withdraw()
    while True:
        file_path = filedialog.askopenfilenames()
        if file_path == '':
            messagebox.showinfo("提示","您没有选择文件")
        else:
            print('选择成功')
            break
    # 储存选择的文件路径
    file_path = str(file_path)[1:-1].split(',')
    with open("path_file.txt", "w") as f: # 清空
        f.writelines([])
    for path in file_path:
        with open("path_file.txt", "a") as f:
            f.writelines(path.strip() + '\n')
    return

def appendpath():
    root = tk.Tk()
    root.withdraw()
    if os.access("path_file.txt", os.F_OK):
        while True:
            file_path = filedialog.askopenfilenames()
            if file_path == '':
                messagebox.showinfo("提示", "您没有选择文件")
            else:
                print('选择成功')
                break
        # 储存选择的文件路径
        file_path = str(file_path)[1:-1].split(',')

        for path in file_path:
            with open("path_file.txt", "a") as f:
                f.writelines(path.strip() + '\n')
    else:
        print('没有配置文件，请转到选择程序选项')
    return


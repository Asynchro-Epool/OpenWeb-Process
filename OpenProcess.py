import os

def openBa():
    with open('path_file.txt','r') as f:
    	if f.readlines != '':
        	for line in f.readlines():
            	line = line.strip().strip('"').strip("'")
            	print(line)
            	os.startfile(line)
        else
        	print('未选择程序')
    return

def webselect():
    with open('path_web.txt', 'a') as f: # 这里是为了 没有文件的新建一个
        f.write('')
        os.startfile('path_web.txt')
    return

def webopen():
    with open('path_web.txt', 'r') as f:
        if f.readlines != '':
        	for line in f.readlines():
            	line = line.strip().strip('"').strip("'")
            	print(line)
            	os.startfile(line)
        else
        	print('未输入网址')
    return
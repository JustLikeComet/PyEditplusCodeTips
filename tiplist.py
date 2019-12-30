import sys
from tkinter import *
from pathlib import Path

def on_closing(*ignore):
	global root
	root.destroy()

def DBMouseLeft(event):
	global root
	global lb
	print(lb.get(lb.curselection()), end='')
	root.destroy()

def EnterKey(key):
	global root
	global lb
	print(lb.get(lb.curselection()), end='')
	root.destroy()

def findInfoFile():
	global currdir
	tempdir = currdir
	while True:
		tempPath = Path(tempdir+"\\Tips.dat")
		if tempPath.exists():
			return tempdir+"\\Tips.dat"
		pos = tempdir.rfind("\\")
		if pos==-1:
			return
		else:
			tempdir = tempdir[0:pos]
	return ""


def loadTipsToList(tipPath, prefix):
	global lb
	fh = open(tipPath, "r")
	while True:
		line = fh.readline()
		if not line:
			break
		if prefix=="" or line.startswith(prefix):
			lb.insert(END, line[0:len(line)-1])
		#print(line[0:len(line)-1], end="")

	fh.close()
	
maindir = "c:\\"
currdir = sys.argv[1]
currWord = sys.argv[2]

root = Tk()
lb = Listbox(root) 
lb.pack(side=LEFT, fill=Y, expand=YES)
#lb.insert('end', "")
#lb.insert(ANCHOR, 'Python', 'Kotlin', 'Swift', 'Ruby', 'sel01', 'sel02', 'sel03', 'sel04', 'sel05', 'sel06', 'sel07', 'sel08', 'sel09', 'sel10')
lb.bind('<Double-1>', DBMouseLeft)
lb.bind('<Return>', EnterKey)
lb.focus_set()
scroll = Scrollbar(root, command=lb.yview)
scroll.pack(side=RIGHT, fill=Y)
lb.configure(yscrollcommand=scroll.set)

root.bind('<Escape>', on_closing)

infopath = findInfoFile()
if infopath != "" :
	loadTipsToList(infopath, currWord)

root.mainloop()


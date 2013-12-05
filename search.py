import symlink
import subprocess as sp
from Tkinter import *
import sys

def callback():
    print e.get()



def get(event):
	top_dir = "/Users/kevin/Desktop/FYMProjectFolder/test_project"
	tmp_dir = "/Users/kevin/temp"

	#symlink.link_tags("/Users/kevin/Desktop/FYMProjectFolder/test_project", "/Users/kevin/Desktop", event.widget.get())
	#open_dir("/Users/kevin/Desktop/tagged_files")
	search_string = event.widget.get()
	search_list = search_string.split(' ')
	tag_string = ''
	project_string = ''

	for x in search_list: 
		if x[0] == '!':
			project_string = x[1:]
		else:
			if tag_string:
				tag_string = tag_string + x + ':'	
			else:
				tag_string = x + ':'

	if project_string:
		if tag_string:
			tag_string = tag_string.rstrip(':')
			symlink.link_project_tags(top_dir, tmp_dir, project_string, tag_string)
		else:
			symlink.link_project_files(top_dir, tmp_dir, project_string)
		open_dir(tmp_dir + "/" + project_string)	

	elif tag_string:
		tag_string = tag_string.rstrip(':')
		symlink.link_tags(top_dir, tmp_dir, tag_string)
		open_dir(tmp_dir + "/" + "tagged_files")

	sys.exit()		



def open_dir(directory):
	sp.call(["open", directory])

master = Tk()

e = Entry(master, width=100)
e.bind('<Return>', get)
e.pack()

e.focus_set()   
mainloop()
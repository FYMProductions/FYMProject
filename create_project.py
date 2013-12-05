#! /usr/bin/python

import symlink
import subprocess as sp
import openmeta
from Tkinter import *
from tkFileDialog import *
import sys
import os

file_names = []
om = openmeta.open_meta()

def callback():
    print e.get()

def get(event):
	search_string = event.widget.get()
	tag_string = search_string.replace(' ', ':')

	print tag_string

	for files in file_names:
		print files
		om.set_maverick_tag(files, tag_string)


	#for files in file_names:
	#	if om.get_meta(files)['tags']:
	#		for x in om.get_meta(files)['tags']:
	#			tag_string = tag_string + ":" + x

	#	print tag_string
	#	om.set_tags(files, tag_string)

	sys.exit()

def open_dir(directory):
	sp.call(["open", directory])

master = Tk()

e = Entry(master, width=100)
e.bind('<Return>', get)
e.pack()

e.focus_set()   

file_names = askopenfilenames(parent=master, title="Choose files for tagging")
print file_names

mainloop()
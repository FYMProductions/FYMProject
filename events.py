#! /usr/bin/python

import os, datetime, time       
import fsevents                 
import Tkinter
import openmeta 

#local_path  = os.getenv('LOCAL_PATH',  '/Users/kevin/Desktop/FYMProjectFolder/test_client')
local_paths = []
root_path = '../fym_clients/'
test_path = os.listdir(root_path)
previous_event = ''

print test_path

for x in test_path:
	if os.path.isdir(root_path + x):
		local_paths.append(root_path + x)
print local_paths

om = openmeta.open_meta()

# list of files to ignore, simple substring match
ignore_list = ['.svn', '.DS_Store', '.git']

def init_tags(event):
	run = True
	global previous_event
	
	print previous_event
	for ig in ignore_list:
		if ig in event.name:
			run = False

	if event.name != previous_event and run == True:

		dir_test = event.name.split('/')
		if event.mask == 256 and dir_test[-3] == 'fym_clients': 
			filename = event.name
			current_dir = filename.split('/')
			client_name = current_dir[-2]

			print client_name
			py_string = 'python tag_dialog.py ' + event.name + ' ' + client_name
			os.system(py_string)

		previous_event = event.name

observers = []

i = 0
for x in local_paths:  
	observers.append(fsevents.Observer())
	observers[i].start()
	fileStream = fsevents.Stream(init_tags, x, file_events=True)
	observers[i].schedule(fileStream)
	i = i + 1
observers.starts()	

#while True:
#    continue
#monitor.starts()
#monitor.unschedule(fileStream)
#monitor.stop()
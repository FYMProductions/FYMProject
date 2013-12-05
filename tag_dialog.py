#! /usr/bin/python

from Tkinter import *
import openmeta
import os
import sys

root_path = "../fym_clients"
client = sys.argv[2]
filename = sys.argv[1]
new_path = ''
project_name = ''



file_types =  {  0 : root_path + '/' + client + '/Assets/Media/2D/Photos/Compressed/',
				 1 : root_path + '/' + client + '/Assets/Media/2D/Photos/RAW/',
				 2 : root_path + '/' + client + '/Assets/Media/2D/textures/',
				 3 : root_path + '/' + client + '/Assets/Media/Audio/Mixes/',
				 4 : root_path + '/' + client + '/Assets/Media/Audio/Music/',
				 5 : root_path + '/' + client + '/Assets/Media/Audio/Production\ Sound/',
				 6 : root_path + '/' + client + '/Assets/Media/Audio/SFX/',
				 7 : root_path + '/' + client + '/Assets/Media/Audio/VO/',
				 8 : root_path + '/' + client + '/Assets/Media/Video/CompressedFiles/',
				 9 : root_path + '/' + client + '/Assets/Media/Video/ProxyFiles/',
				10 : root_path + '/' + client + '/Assets/Media/Video/RawFiles/',
				11 : root_path + '/' + client + '/Assets/WorkingFiles/After\ Effect/',
				12 : root_path + '/' + client + '/Assets/WorkingFiles/Cinema4D/',
				13 : root_path + '/' + client + '/Assets/WorkingFiles/Illustrator/',
				14 : root_path + '/' + client + '/Assets/WorkingFiles/Photoshop/',
				15 : root_path + '/' + client + '/Assets/WorkingFiles/Premiere/',
				16 : root_path + '/' + client + '/Documents/Financials/AccountsPayable/',
				17 : root_path + '/' + client + '/Documents/Financials/AccountsReceivable/',
				18 : root_path + '/' + client + '/Documents/Financials/Budgets/',
				19 : root_path + '/' + client + '/Documents/Financials/POs/',
				20 : root_path + '/' + client + '/Documents/Notes/',
				21 : root_path + '/' + client + '/Documents/ProjectManagement/Contacts/',
				22 : root_path + '/' + client + '/Documents/ProjectManagement/Proposal/',
				23 : root_path + '/' + client + '/Documents/ProjectManagement/RFPs/',
				24 : root_path + '/' + client + '/Documents/ProjectManagement/TaskOutlines/',
				25 : root_path + '/' + client + '/Documents/ProjectManagement/Timeline/',
				26 : root_path + '/' + client + '/Documents/ProjectManagement/Timesheets/',
				27 : root_path + '/' + client + '/Documents/ReferenceMaterial/',
				28 : root_path + '/' + client + '/Documents/StyleGuide/', 
				29 : root_path + '/' + client + '/Assets/Templates/',
				30 : root_path + '/' + client + '/Assets/WorkingFiles/After\ Effect/PreviewCacheAutoSaveEtc/',
				31 : root_path + '/' + client + '/Assets/WorkingFiles/After\ Effect/Renders/',
				32 : root_path + '/' + client + '/Assets/WorkingFiles/Premiere/PreviewCacheAutoSaveEtc/',
				33 : root_path + '/' + client + '/Documents/Scripts/',
				34 : root_path + '/' + client + '/MasteredProjects/',
				35 : root_path + '/' + client + '/Assets/WorkingFiles/'
}

om = openmeta.open_meta()

def file_place(projectname):
	global new_path
	type_set = 0
	#print os.getcwd()
	print new_path

	new_file = filename.split('/')
	file_tags = om.get_maverick_tag(filename)

	om.set_maverick_tag(filename, projectname)

	print file_tags
	print new_path
	if not os.path.exists(new_path):
		os.makedirs(new_path)

	os.rename(filename, new_path + '/' + new_file[-1])

	'''i = 0
	while i < len(file_extensions):
		for x in file_extensions[i]:
			if x in filename:
				type_set = 1
				print "file: " + filename 
				print "belongs: " + file_types[i]
		i = i + 1		
	'''

	#print file_tags

	sys.exit()

def test():
	print "test works"

def tag_dialog(event):
	global project_name
	project_name = event.widget.get()
	print project_name
	master = Tk()
	menu_bar = Menu(master)

	asset_menu = Menu(menu_bar, tearoff=0)
	menu_bar.add_cascade(label='Assets', menu=asset_menu)

	photo_menu = Menu(asset_menu, tearoff=0)
	asset_menu.add_cascade(label='Photos', menu=photo_menu)
	photo_menu.add_command(label='Compressed', command=compressed_menu)
	photo_menu.add_command(label='Raw', command=raw_menu)

	text_menu = Menu(asset_menu, tearoff=0)
	asset_menu.add_cascade(label='Textures', menu=text_menu)

	audio_menu = Menu(text_menu, tearoff=0)
	text_menu.add_cascade(label='Audio', menu=audio_menu)
	audio_menu.add_command(label='Mixes', command=mix_menu)
	audio_menu.add_command(label='Music', command=music_menu)
	audio_menu.add_command(label='ProductionSound', command=prod_menu)
	audio_menu.add_command(label='SFX', command=sfx_menu)
	audio_menu.add_command(label='VO', command=vo_menu)

	video_menu = Menu(asset_menu, tearoff=0)
	asset_menu.add_cascade(label='Video', menu=video_menu)
	video_menu.add_command(label='CompressedFiles', command=com_menu)
	video_menu.add_command(label='ProxyFiles', command=prox_menu)
	video_menu.add_command(label='RawFiles', command=rawvid_menu)

	asset_menu.add_command(label='Templates', command=temp_menu)

	work_menu = Menu(menu_bar, tearoff=0)
	menu_bar.add_cascade(label='WorkingFiles', menu=work_menu)

	effect_menu = Menu(work_menu, tearoff=0)
	work_menu.add_cascade(label='After Effects', menu=effect_menu)
	effect_menu.add_command(label='PreviewCacheAutoSaveEtc', command=preview_effect_menu)
	effect_menu.add_command(label='Renders', command=render_menu)

	work_menu.add_command(label='Cinema4D', command=cinema_menu)
	work_menu.add_command(label='Illustrator', command=illustrator_menu)
	work_menu.add_command(label='Photoshop', command=photoshop_menu)

	prem_menu = Menu(work_menu, tearoff=0)
	work_menu.add_cascade(label='Premiere', menu=prem_menu) 
	prem_menu.add_command(label='PreviewCacheAutoSaveEtc', command=preview_prem_menu)

	doc_menu = Menu(menu_bar, tearoff=0)
	menu_bar.add_cascade(label='Documents', menu=doc_menu)

	fin_menu = Menu(doc_menu, tearoff=0)
	doc_menu.add_cascade(label='Financials', menu=fin_menu)
	fin_menu.add_command(label='AccountsPayable', command=acct_pay)
	fin_menu.add_command(label='AccountsReceivable', command=acct_rec)
	fin_menu.add_command(label='Budgets', command=budget)
	fin_menu.add_command(label='POs', command=pos_menu)

	asset_menu.add_command(label='Scripts', command=script_menu)
	asset_menu.add_command(label='Notes', command=note_menu)

	proj_menu = Menu(doc_menu, tearoff=0)
	doc_menu.add_cascade(label='ProjectManagement', menu=proj_menu)
	proj_menu.add_command(label='Contacts', command=contact_menu)
	proj_menu.add_command(label='Proposal', command=proposal_menu)
	proj_menu.add_command(label='RFPs', command=rfp_menu)
	proj_menu.add_command(label='TaskOutlines', command=task_menu)
	proj_menu.add_command(label='Timeline', command=timeline_menu)
	proj_menu.add_command(label='Timesheets', command=timesheet_menu)
	proj_menu.add_command(label='ReferenceMaterial', command=reference_menu)
	proj_menu.add_command(label='StyleGuide', command=style_menu)

	menu_bar.add_command(label='MasteredProjects', command=master_menu)


	menu_bar.post(500,100)
	
	#om.set_tags(sys.argv[1], event.widget.get())
	file_place(project_name)

def compressed_menu():
	global new_path
	global project_name
	
	new_path = file_types[0] + project_name
	return True	


def raw_menu():
	global new_path
	global project_name
	
	new_path = file_types[1] + project_name
	return True
def mix_menu():
	global new_path
	global project_name
	
	new_path = file_types[3] + project_name
	return True
def music_menu():
	global new_path
	global project_name
	
	new_path = file_types[4] + project_name
	return True
def prod_menu():
	global new_path
	global project_name
	
	new_path = file_types[5] + project_name
	return True
def sfx_menu():
	global new_path
	global project_name
	
	new_path = file_types[6] + project_name
	return True
def vo_menu():
	global new_path
	global project_name
	
	new_path = file_types[7] + project_name
	return True
def com_menu():
	global new_path
	global project_name
	
	new_path = file_types[8] + project_name
	return True
def prox_menu():
	global new_path
	global project_name
	
	new_path = file_types[9] + project_name
	return True
def rawvid_menu():
	global new_path
	global project_name
	
	new_path = file_types[10] + project_name
	return True
def temp_menu():
	global new_path
	global project_name
	
	new_path = file_types[29] + project_name
	return True

#def work_menu():
#	global new_path
#	global project_name
#	
#	new_path = file_types[35] + project_name
#	return True

def preview_effect_menu():
	global new_path
	global project_name
	
	new_path = file_types[30] + project_name
	return True
def render_menu():
	global new_path
	global project_name
	
	new_path = file_types[31] + project_name
	return True
def cinema_menu():
	global new_path
	global project_name
	
	new_path = file_types[12] + project_name
	return True
def illustrator_menu():
	global new_path
	global project_name
	
	new_path = file_types[13] + project_name
	return True
def photoshop_menu():
	global new_path
	global project_name
	
	new_path = file_types[14] + project_name
	return True
def preview_prem_menu():
	global new_path
	global project_name
	
	new_path = file_types[32] + project_name
	return True
def acct_pay():
	global new_path
	global project_name
	
	new_path = file_types[16] + project_name
	return True
def acct_rec():
	global new_path
	global project_name
	
	new_path = file_types[17] + project_name
	return True

def budget():
	global new_path
	global project_name
	
	new_path = file_types[18] + project_name
	return True

def pos_menu():
	global new_path
	global project_name
	
	new_path = file_types[19] + project_name
	return True

def script_menu():
	global new_path
	global project_name
	
	new_path = file_types[33] + project_name
	return True
	
def note_menu():
	global new_path
	global project_name
	
	new_path = file_types[20] + project_name
	return True
def contact_menu():
	global new_path
	global project_name
	
	new_path = file_types[21] + project_name
	return True
def proposal_menu():
	global new_path
	global project_name
	
	new_path = file_types[22] + project_name
	return True
def rfp_menu():
	global new_path
	global project_name
	
	new_path = file_types[23] + project_name
	return True
def task_menu():
	global new_path
	global project_name
	
	new_path = file_types[24] + project_name
	return True
def timesheet_menu():
	global new_path
	global project_name
	
	new_path = file_types[26] + project_name
	return True
def timeline_menu():
	global new_path
	global project_name
	
	new_path = file_types[25] + project_name
	return True
def reference_menu():
	global new_path
	global project_name
	
	new_path = file_types[27] + project_name
	return True
def style_menu():
	global new_path
	global project_name
	
	new_path = file_types[28] + project_name
	return True
def master_menu():
	global new_path
	global project_name
	
	new_path = file_types[34] + project_name
	return True	


new_master = Tk()

#new_master.config(menu=menu_bar)
label = Label(new_master, text='Project Name')
label.pack(side=LEFT)

e = Entry(new_master, width=100)
e.bind('<Return>', tag_dialog)
e.pack(side=RIGHT)

e.focus_set() 
new_master.mainloop()
#! /usr/bin/python
#-----------------------#
# Symbolic Link Creator #
#-----------------------#

import os
import openmeta
import shutil as sh

def link_project_files(startpath, endpath, project):
	project_dir = os.path.join(endpath + "/" + project)

	if not os.path.exists(project_dir):
		print project_dir
		os.makedirs(project_dir)
	else:
		sh.rmtree(project_dir)
		os.makedirs(project_dir)

	for root, dirs, files in os.walk(startpath):
		print root
		for x in files:
			fileList = x.split('_')

			if fileList[0] == project:
				project_file = os.path.join(root, x)				
				os.symlink(project_file, project_dir + "/" + fileList[1])	



def link_project_tags(startpath, endpath, project, tags):
	project_dir = os.path.join(endpath + "/" + project)

	if not os.path.exists(project_dir):
		#print project_dir
		os.makedirs(project_dir)
	else:
		sh.rmtree(project_dir)
		os.makedirs(project_dir)

	for root, dirs, files in os.walk(startpath):
		print files

		tagged_files = project_tags(startpath, endpath, tags)
		for x in files:
			fileList = x.split('_')

			if fileList[0] == project:
				for a in tagged_files:
					if a == x:
						project_file = os.path.join(root, x)
						os.symlink(project_file, project_dir + "/" + fileList[1])	



def link_tags(startpath, endpath, tags):
	project_dir = os.path.join(endpath + "/" + "tagged_files")

	if not os.path.exists(project_dir):
		#print project_dir
		os.makedirs(project_dir)
	else:
		sh.rmtree(project_dir)
		os.makedirs(project_dir)
	
	tagged_files = project_tags(startpath, endpath, tags)
		
	for x in tagged_files:
		split_dir = x.split('/')
		print x
		print split_dir[-1]
		os.symlink(x, project_dir + "/" + split_dir[-1])



def project_tags(startpath, endpath, tags):
	om = openmeta.open_meta()
	return om.search_tags(startpath, tags)

meta = openmeta.open_meta()

#meta.set_tags("/Users/kevin/Desktop/FYMProjectFolder/test_project/projectname_file.txt", "filetype:companyname:testtag")
#link_tags("/Users/kevin/Desktop/FYMProjectFolder/test_project", "/Users/kevin/Desktop", "testtag")
#link_project_tags("/Users/kevin/Desktop/FYMProjectFolder/test_project","/Users/kevin/Desktop", "newproject", "companyname")
#project_tags("/Users/kevin/Desktop/FYMProjectFolder/test_project","/Users/kevin/Desktop", , "testtag")


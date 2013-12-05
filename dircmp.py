#! /usr/bin/python
from filecmp import *
import os, shutil

def treecopy(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            treecopy(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d) or os.stat(src).st_mtime - os.stat(dst).st_mtime > 1:
                shutil.copy2(s, d)

def print_diff_files(dcmp):
	for name in dcmp.diff_files:
		print "different file %s found in %s and %s" % (name, dcmp.left, dcmp.right)

	for sub_dcmp in dcmp.subdirs.values():
		print_diff_files(sub_dcmp)

def diff(list1, list2):
    c = set(list1).union(set(list2))
    d = set(list1).intersection(set(list2))
    return list(c - d)

dcmp = dircmp('dir1', 'dir2')

#dcmp.report_full_closure()

#print dcmp.left_list
#print dcmp.right_list

#different = diff(dcmp.left_list, dcmp.right_list)
#print different

#for x in different:
#	filePath = "dir2/" + x
#	if os.path.isdir(filePath):
#		print filePath + " is a directory\n"
#		print os.listdir(filePath)
#	elif os.path.isfile(filePath):
#		print filePath + " is a file\n"
#	else:
#		print filePath + " doesn not seem to exist??\n"

print_diff_files(dcmp)
treecopy("dir2", "dir1", False, None)
#! /usr/bin/python
import re
import os
import sys

newFile = open('Hierarchy', 'r')
pattern = r'(\w)'
commaString =""
currentLevel = 0
filePath = ""
topDir = ""

while True:
	fileString = newFile.readline()
	tabLength = len(fileString) - len(fileString.strip())
	#print tabLength

	fileString = fileString.strip()
	fileString = re.sub('^[0-9]\.+', '',fileString)
	fileString = fileString.strip()

	topDir = fileString

	comma = re.findall(r',', fileString)

	if currentLevel == 0:
		filePath = fileString
		os.mkdir(filePath, 0755)
		currentLevel = currentLevel + 1
		oldLength = tabLength

	elif not re.findall(r'\*',fileString):
		if tabLength > oldLength:
			filePath = filePath + "/" + fileString
			os.mkdir(filePath, 0755)
			print "make: " + filePath
			oldLength = tabLength

		elif tabLength < oldLength:
			if oldLength - tabLength > 8:
				dirLength = (oldLength - tabLength)/8
				dirList = filePath.split('/')
				newPath = ""

				for b in dirList:
					if b == '':
						dirList.remove(b)

				#print "dirLength: " + str(dirLength)
				#print "listLength: " + str(len(dirList))
				#print dirList

				i=0
				while i < (len(dirList)-(dirLength))-1:
					if i == 0:
						newPath = newPath + dirList[i]
					else:
						newPath = newPath + '/' + dirList[i]

					#print "dirList: " + newPath
					i=i+1
				filePath = newPath + '/' + fileString
				
				print "Path: " + filePath

			else:
				dirList = filePath.split('/')
				newPath = ""

				for b in dirList:
					if b == '':
						dirList.remove(b)

				i=0
				while i < (len(dirList)-2):
					if i == 0:
						newPath = dirList[i] 
					else:	
						newPath = newPath + '/' + dirList[i]
					#print dirList[i]
					i=i+1

				filePath = newPath + '/' + fileString
			
			os.mkdir(filePath, 0755)
			oldLength = tabLength

		else:
			print "filePath: " + filePath
			dirList = filePath.split('/')
			newPath = ""


			for b in dirList:
					if b == '':
						dirList.remove(b)

			#print dirList

			i=0
			while i < (len(dirList)-1):
				if i == 0:
					newPath = dirList[i]
				else:
					newPath = newPath + '/' + dirList[i]				
				#print newPath
				i=i+1

			filePath = newPath + '/' + fileString
			os.mkdir(filePath, 0755)
			print "create dir: " + filePath

			oldLength = tabLength

		#print fileString


	#if len(comma) > 0:
	#	tabLength = len(fileString) - len(fileString.strip())
	#	tabString = " " * tabLength
	#	commaString = re.sub(',', '\n' + tabString, fileString)
	
	#	print commaString
	#else:
	#	print fileString

	if len(fileString) == 0:
		break

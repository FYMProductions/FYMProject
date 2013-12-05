#!/usr/bin/python
import openmeta
from os import *
from os.path import *

def find_tags():
	filePath = './'
	fileName = ''
	myTags = ''

	for x in listdir(filePath):
		fileName = join(filePath, x)

		if isfile(fileName):
			myList = openmeta.get_meta(fileName)['tags']
			if myList:
				for i in myList:
					myTags = myTags + i + ' '
				print fileName + " has tags: " + myTags
			else:	
				print fileName

def search_tags(filePath, searchTags):
	myTags = ''

	for x in listdir(filePath):
		fileName = join(filePath, x)

		if isfile(fileName):
			myList = openmeta.get_meta(fileName)['tags']
			if myList:
				for i in myList:
					for a in searchTags:
						if a == i:
							myTags = myTags + i + ' '

				print fileName + " has tags: " + myTags			

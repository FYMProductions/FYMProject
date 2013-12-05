#!/usr/bin/env python

from os import *
from os.path import *
import os
import subprocess
from subprocess import Popen, PIPE
import shlex

class open_meta:

    def has_tags(self, filename):
        if os.popen('tag -N ' + filename).read().strip():
            return True
        else:
            return False    

    def set_maverick_tag(self, filename, tag_string):
        os.popen('tag -s ' + tag_string + ' ' + filename)

    def add_maverick_tag(self, filename, tag_string):
        os.popen('tag -a ' + tag_string + ' ' + filename)  

    def get_maverick_tag(self, filename):
        return os.popen('tag -N ' + filename).read().strip().split(',')  


    def check_openmeta(self):
        try:
            Popen('tag', stdout=PIPE, stderr=PIPE).communicate()
            return True
        except OSError:
            return False

    def path_check(self,filename):
        return os.path.realpath(os.path.join('.', filename))
        
    def cli_openmeta(self, filename, *extra_args):
        #print filename
        doSet = 0
        tag_string = ''

        for x in extra_args:
            if x == '-s':
                doSet = 1
            else:
                tag_string = tag_string + x    


        cli_args = ['openmeta']
        if doSet:
            cli_args.append('-s')
            cli_args.append(tag_string)
        else:    
            cli_args.extend(extra_args)

        #cli_args.append('-p')
        cli_args.append(self.path_check(filename))
        
        final_args = ' '.join(cli_args)
        #print final_args

        proc = Popen(cli_args,stdout=PIPE)
        
        stdout, stderr = proc.communicate()
        return stdout
        
    def parse(self,clioutputstring):   
        metadata = {}
        lines = clioutputstring.splitlines()
        print lines
        tags = shlex.split(lines[1][6:])
        rating_string = lines[2][8:]
        
        try:
            rating = float(rating_string)
        except ValueError:
            rating = 0

        metadata['tags'] = tags
        metadata['rating'] = rating
        return metadata
        
    def get_meta(self, filename):
        #print self.cli_openmeta(filename)
        return self.parse(self.cli_openmeta(filename))

    def set_tags(self, filename, tags):
        self.cli_openmeta(filename, '-s', *tags)

    def find_tags(self):
        filePath = './'
        fileName = ''
        myTags = ''

        for x in listdir(filePath):
            fileName = join(filePath, x)

            if isfile(fileName):
                myList = self.get_meta(fileName)['tags']
                print mylist
                if myList:
                    for i in myList:
                        myTags = myTags + i 
                    print fileName + " has tags: " + myTags
                else:   
                    print fileName

    def search_tags(self, filePath, searchTags):
        myTags = ''
        tagged_files = []
        tags = searchTags.split(':')
        #print "search tags: "
        print tags
        count = 0

        #for x in listdir(filePath):
        for root, dirs, files in os.walk(filePath):
            count = 0
            for x in files:
                fileName = join(root, x)

                if isfile(fileName):
                    myList = self.get_meta(fileName)['tags']
                    #print myList
                    if myList:
                        for i in myList:
                            split_tags = i.split(':')

                            if set(tags).issubset(set(split_tags)):
                                #print "true"
                                tagged_files.append(root + "/" + x)

        return tagged_files            

    

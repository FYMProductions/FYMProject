#!/usr/bin/env python

import os.path
import subprocess
from subprocess import Popen, PIPE
import shlex

class open_meta:

    def check_openmeta():
        try:
            Popen('openmeta', stdout=PIPE, stderr=PIPE).communicate()
            return True
        except OSError:
            return False

    def path_check(filename):
        return os.path.realpath(os.path.join('.', filename))
        
    def cli_openmeta(filename, *extra_args):
        cli_args = ['openmeta']
        cli_args.extend(extra_args)
        cli_args.append('-p')
        cli_args.append(path_check(filename))
        
        proc = Popen(cli_args,stdout=PIPE)
        
        stdout, stderr = proc.communicate()
        return stdout
        
    def parse(clioutputstring):   
        metadata = {}
        lines = clioutputstring.splitlines()
        tags = shlex.split(lines[1][6:])
        rating_string = lines[2][8:]
        
        try:
            rating = float(rating_string)
        except ValueError:
            rating = 0

        metadata['tags'] = tags
        metadata['rating'] = rating
        return metadata
        
    def get_meta(filename):
        return parse(cli_openmeta(filename))

    def set_tags(filename, tags):
        cli_openmeta(filename, '-s', *tags)

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

    

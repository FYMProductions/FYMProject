#! /usr/bin/python

import os, datetime, time, fsevents, Tkinter, socket, filecmp, shutil
import os.path, subprocess, shlex       

rsync_pass = "password"
local_path  = os.getenv('LOCAL_PATH',  '/Users/kevin/tmp/')
remote_host = os.getenv('REMOTE_HOST', 'kevin@localhost')
remote_path = os.getenv('REMOTE_PATH', '/Users/kevin/newtmp/')

ignore_list = ['.svn', '.DS_Store', '.git']

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

class Server:
	gate = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = socket.gethostname()
	port = 1111

	def __init__(self, port):
		self.port = port
		self.gate.bind((self.host, self.port))  
		self.listen()

	def listen(self):
		self.gate.listen(10)
		while True:
			conn,address = self.gate.accept()

def display(str):
    global ta
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mystr = "[{0}] {1} \n".format(now, str)
    ta.insert(Tkinter.END, mystr)


def fileSync(event):
    filename = event.name
    remote_file = filename.replace(local_path, '')
    for ig in ignore_list:                          
        if ig in filename:
            return
    
    print local_path
    print remote_path

    cmd = " sshpass -p '%s' rsync -avz --delete %s %s:%s " % (rsync_pass, local_path, remote_host, remote_path)
    #cmd = "tail -f test.txt"
    display("Syncing %s " % filename)
    #proc = os.popen('tail test.txt').read()
    #print proc
    #display(proc)
    os.system(cmd)


canvas = Tkinter.Tk()
scroll = Tkinter.Scrollbar(canvas)
ta = Tkinter.Text(canvas)

scroll.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
ta.pack(side=Tkinter.LEFT, fill=Tkinter.Y)
scroll.config(command=ta.yview)
ta.config(yscrollcommand=scroll.set)

monitor = fsevents.Observer()
monitor.start()
fileStream = fsevents.Stream(fileSync, local_path, file_events=True)
monitor.schedule(fileStream)

display("Monitoring: %s " % local_path)
canvas.mainloop()

monitor.unschedule(fileStream)
monitor.stop()
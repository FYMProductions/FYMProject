#! /usr/bin/python

from fsevents import Observer, Stream
import signal

def event_callback(event):
    filename = event.name
    print "Filename: ", event.name

def clean_exit(signal, frame):
    global observer, stream
    observer.unschedule(stream)
    observer.stop()

observer = Observer()
observer.start()
stream = Stream(event_callback, "~/tmp/", file_events=True)
observer.schedule(stream)

# run until ctrl-c
signal.signal(signal.SIGINT, clean_exit)
signal.pause()
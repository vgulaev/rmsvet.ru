import threading
import os.path
import os

class rl(object):
    files = []    

def reloadserver( filename ):
    os._exit(3)

def watch_file( filename, callback = reloadserver ):
    rl.files += [ { "name" : filename , "timem" : os.path.getmtime( filename ), "callback" : callback } ]

def file_modify():
    res = False
    for e in rl.files:
        if e[ "timem" ] != os.path.getmtime( e[ "name" ] ):
            print( "Modify : {fn}".format( fn = e[ "name" ] ), " call: ", e[ "callback" ] )
            e[ "callback" ]( filename = e[ "name" ] )
    return res

def start_watch():
    if file_modify():
        pass
    else:
        threading.Timer( 2.0, start_watch ).start()

def watch_all_in_set(set):
    for i in set:
        watch_file(i)
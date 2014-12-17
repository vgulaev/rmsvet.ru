import sys
import threading
import os.path
import os
import sys
class rl(object):
    files = []    

def watch_file( filename ):
    rl.files += [ { "name" : filename , "timem" : os.path.getmtime( filename ) } ]

def file_modify():
    res = False
    for e in rl.files:
        if e[ "timem" ] != os.path.getmtime( e[ "name" ] ):
            print( "Modify : {fn}".format( fn = e[ "name" ] ) )
            res = True
            break
    return res
def start_watch():
    if file_modify():
        os._exit(3)
    else:
        threading.Timer( 2.0, start_watch ).start()
# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime
import projectorium.reloader
from myhttpd.HTTPRequestHandler import HTTPRequestHandler

projectorium.reloader.watch_file( "srvapp3.py" )
projectorium.reloader.watch_file( "projectorium/reloader.py" )
projectorium.reloader.watch_file( "myhttpd/HTTPRequestHandler.py" )

projectorium.reloader.start_watch()
#projectorieloader.

def run( server_class = HTTPServer, handler_class = HTTPRequestHandler ):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    print( "Start at {date}".format(date = datetime.datetime.now()) )
    run()
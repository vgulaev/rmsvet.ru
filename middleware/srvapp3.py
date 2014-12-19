# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime
import projectorium.reloader
from myhttpd.HTTPRequestHandler import HTTPRequestHandler
import sett
import dbclasses.dbworker
import dbclasses.dbobj
import common

dbclasses.dbworker.cred = dbclasses.dbworker.loadmysqlcredential( sett )

projectorium.reloader.watch_file( "srvapp3.py" )
projectorium.reloader.watch_file( "projectorium/reloader.py" )
projectorium.reloader.watch_file( "myhttpd/HTTPRequestHandler.py" )
projectorium.reloader.watch_file( "wsservers.py" )
projectorium.reloader.watch_file( "staticcontentgenerator.py" )

projectorium.reloader.start_watch()
#projectorieloade

def run( server_class = HTTPServer, handler_class = HTTPRequestHandler ):
    server_address = ( sett.host, sett.port )
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    common.detect_common_env()
    print( "Start at {date}".format(date = datetime.datetime.now()) )
    run()
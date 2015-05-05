# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert( 0, os.path.dirname(os.path.abspath( __file__ ) ) )
import datetime
from http.server import HTTPServer
from myhttpd.HTTPRequestHandler import HTTPRequestHandler
import sett
import common
import projectorium.reloader
import projectorium.rerender
import dbclasses.dbworker

dbclasses.dbworker.cred = dbclasses.dbworker.loadmysqlcredential( sett )
set = []
set.append( "srvapp3.py" )
set.append( "common.py" )
set.append( "projectorium/reloader.py" )
set.append( "projectorium/rerender.py" )
set.append( "myhttpd/HTTPRequestHandler.py" )
set.append( "wsservers.py" )
set.append( "staticcontentgenerator.py" )
set.append( "statistics.py" )
set.append( "html/templates/index.mako" )
set.append( "html/templates/orders.mako" )
set.append( "html/templates/contact.mako" )
set.append( "html/templates/cart.mako" )
set.append( "html/templates/allorders.mako" )
set.append( "html/templates/bible.mako" )
set.append( "html/templates/cardrules.mako" )
set.append( "html/templates/stat.mako" )
set.append( "html/templates/global-vals.tmpl" )
set.append( "../bible.md" )
set.append( "html/templates/html5-doc.tmpl" )
set.append( "html/templates/ezsp_for_everybody.mako" )
set.append( "html/templates/ezsp_for_everybody/content.tmpl" )

projectorium.reloader.watch_all_in_set(set)
projectorium.reloader.start_watch()
projectorium.rerender.rerenderall()

def run( server_class = HTTPServer, handler_class = HTTPRequestHandler ):
    handler_class.server_version = "EWS"
    handler_class.sys_version = "0.1 beta"
    server_address = ( sett.host, sett.port )
    httpd = server_class( server_address, handler_class )
    httpd.serve_forever()

if __name__ == '__main__':
    common.detect_common_env()
    print( "Start at {date}".format( date = datetime.datetime.now()) )
    run()
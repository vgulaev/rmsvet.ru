# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import datetime
from http.server import HTTPServer
from myhttpd.HTTPRequestHandler import HTTPRequestHandler
import sett
import common
import projectorium.reloader
import projectorium.rerender
import dbclasses.dbworker

dbclasses.dbworker.cred = dbclasses.dbworker.loadmysqlcredential( sett )

projectorium.reloader.watch_file( "srvapp3.py" )
projectorium.reloader.watch_file( "common.py" )
projectorium.reloader.watch_file( "projectorium/reloader.py" )
projectorium.reloader.watch_file( "projectorium/rerender.py" )
projectorium.reloader.watch_file( "myhttpd/HTTPRequestHandler.py" )
projectorium.reloader.watch_file( "wsservers.py" )
projectorium.reloader.watch_file( "staticcontentgenerator.py" )
projectorium.reloader.watch_file( "statistics.py" )

projectorium.reloader.watch_file( "html/templates/index.mako" )
projectorium.reloader.watch_file( "html/templates/orders.mako" )
projectorium.reloader.watch_file( "html/templates/contact.mako" )
projectorium.reloader.watch_file( "html/templates/cart.mako" )
projectorium.reloader.watch_file( "html/templates/bible.mako" )
projectorium.reloader.watch_file( "html/templates/cardrules.mako" )
projectorium.reloader.watch_file( "html/templates/global-vals.tmpl" )
projectorium.reloader.watch_file( "../bible.md" )
projectorium.reloader.watch_file( "html/templates/html5-doc.tmpl" )
projectorium.reloader.watch_file( "html/templates/ezsp_for_everybody.mako" )
projectorium.reloader.watch_file( "html/templates/ezsp_for_everybody/content.tmpl" )

projectorium.reloader.start_watch()

projectorium.rerender.rerenderall()
#projectori

def run( server_class = HTTPServer, handler_class = HTTPRequestHandler ):
    server_address = ( sett.host, sett.port )
    httpd = server_class( server_address, handler_class )
    httpd.serve_forever()

if __name__ == '__main__':
    common.detect_common_env()
    print( "Start at {date}".format(date = datetime.datetime.now()) )
    run()
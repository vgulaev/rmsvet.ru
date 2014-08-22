import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import checkrestart
from paste.wsgilib import dump_environ
from paste.auth.digest import digest_password, AuthDigestHandler
import paste.reloader

paste.reloader.install()
paste.reloader.watch_file("checkrestart.py")
paste.reloader.watch_file("index.html")

html = open("index.html", "r").read()
"""
<!DOCTYPE html>

"""

def application(environ, start_response):
    status = '200 OK'
    output = 'Hello World my friend!'

    headers = [('Content-type', 'text/html, charset=UTF-8')]

    start_response(status, headers)

    ret = ["%s: %s\n" % (key, value)
           for key, value in environ.iteritems()]
    
    print "Hello"
    #return [checkrestart.upp() + "ff"]
    return [html]

#
if __name__ == '__main__':
    from paste import httpserver
    #httpserver.serve(AuthDigestHandler(dump_environ, realm, authfunc), host='127.0.0.1', port='8080')
    httpserver.serve(application, host='127.0.0.1', port='8080')
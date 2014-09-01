# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

#import checkrestart
import wsservers as ws
import sitedb
import paste.reloader
paste.reloader.install()
paste.reloader.watch_file("checkrestart.py")
paste.reloader.watch_file("index.html")
paste.reloader.watch_file("sitedb.py")
paste.reloader.watch_file("wsservers.py")

def response_from_file(filename):
    t = open(filename, "r")
    return t.read()

def application(environ, start_response):
    status = '200 OK'
    output = 'Hello World my friend!'

    headers = [('Content-type', 'text/html, charset=UTF-8')]

    start_response(status, headers)

    ret = ["%s: %s\n" % (key, value)
           for key, value in environ.iteritems()]
    
    
    url = environ["PATH_INFO"]
    if url == "/":
        html = response_from_file("index.html")
    elif url == "/libs/jquery/jquery-2.1.1.js":
        #html = response_from_file("libs/jquery/jquery-2.1.1.js")
        html = response_from_file("libs/jquery/jquery-2.1.1.min.js")
        #html = "(){}"
    elif url == "/my.js":
        html = response_from_file("my.js")
    elif url == "/ws/autocomplate":
        #html = str(ret)
        import cgi
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        post = cgi.FieldStorage(
                                fp=environ['wsgi.input'],
                                environ=post_env,
                                keep_blank_values=True
                                )
        #html = str(post)
        #html = post["table"]
        
        tb = post.getvalue("table")
        ft = post.getvalue("filter")

        html = ws.auto_complate(tb, ft)
    else:
        html = url

    return [html]

#
if __name__ == '__main__':
    from paste import httpserver
    from paste.exceptions import errormiddleware
    from paste import evalexception
    #app = errormiddleware.ErrorMiddleware(application, debug=True)
    app = evalexception.EvalException(application)
    #httpserver.serve(AuthDigestHandler(dump_environ, realm, authfunc), host='127.0.0.1', port='8080')
    httpserver.serve(app, host='127.0.0.1', port='8080')
# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import cgi

import paste.reloader
paste.reloader.install()
paste.reloader.watch_file("checkrestart.py")
paste.reloader.watch_file("index.html")
paste.reloader.watch_file("sitedb.py")
paste.reloader.watch_file("wsservers.py")

#own libs
import wsservers as ws
import common
import staticcontentgenerator as scg

def application(environ, start_response):
    status = '200 OK'
    output = 'Hello World my friend!'

    headers = [('Content-type', 'text/html, charset=UTF-8')]

    start_response(status, headers)

    ret = ["%s: %s\n" % (key, value)
           for key, value in environ.iteritems()]
    
    url = environ["PATH_INFO"]
    #print url
    #print "smal:", url[0:6]
    if url[0:6] == "/html/":
        html = common.read_file_to_str(url[1:])
    elif url[0:9] == "/catalog/":
        html = scg.goods_main_view(url)
    elif url == "/":
        html = common.read_file_to_str("index.html")
    elif url == "/libs/jquery/jquery-2.1.1.js":
        #html = response_from_file("libs/jquery/jquery-2.1.1.js")
        html = common.read_file_to_str("libs/jquery/jquery-2.1.1.min.js")
        #html = "(){}"
    elif url == "/js/my.js":
        html = common.read_file_to_str("js/my.js")
    elif url == "/ws/autocomplate":
        #html = str(ret)
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        post = cgi.FieldStorage(
                                fp=environ['wsgi.input'],
                                environ=post_env,
                                keep_blank_values=True
                                )
        
        tb = post.getvalue("table")
        ft = post.getvalue("filter")

        html = ws.auto_complate(tb, ft)
    else:
        html = url
        #html = url[0:6]

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
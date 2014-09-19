# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import cgi

import paste.reloader
paste.reloader.install()
paste.reloader.watch_file("checkrestart.py")
#paste.reloader.watch_file("index.html")
paste.reloader.watch_file("sitedb.py")
paste.reloader.watch_file("wsservers.py")
paste.reloader.watch_file("staticcontentgenerator.py")
paste.reloader.watch_file("sett.py")
paste.reloader.watch_file("statistics.py")

#own libs
import wsservers as ws
import common
import staticcontentgenerator as scg
import sett

def standart_response(start_response, ct):
    status = '200 OK'
    headers = [('Content-type', ct + ', charset=UTF-8')]
    start_response(status, headers)

def detect_common_env( domain ):
    d = common.domains_sql()
    if d.find(caption = domain):
        o = common.organization_sql()
        if o.find(id = d.organization_id.val):
            common.env["organization"] = o

def make_json_ans( url , environ):
    html = ""
    if url == "/ws/autocomplate":
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
    elif url == "/ws/getfilters":
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        post = cgi.FieldStorage(
                                fp=environ['wsgi.input'],
                                environ=post_env,
                                keep_blank_values=True
                                )
        ft = post.getvalue("filter")
        html = ws.getfilters(ft)
    elif url == "/ws/ezsp-query":
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        post = cgi.FieldStorage(
                                fp=environ['wsgi.input'],
                                environ=post_env,
                                keep_blank_values=True
                                )
        eq = post.getvalue("ezsp-query")
        html = ws.ezspquery( eq )
    elif url == "/ws/ezsp-query-filters-value":
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        post = cgi.FieldStorage(
                                fp=environ['wsgi.input'],
                                environ=post_env,
                                keep_blank_values=True
                                )
        eq = post.getvalue("ezsp-query")
        html = ws.ezsp_get_filters_value( eq )

    return html

def application(environ, start_response):
    ret = ["%s: %s\n" % (key, value)
           for key, value in environ.iteritems()]
    #ret = [environ["HTTP_HOST"]]
    ###
    detect_common_env(environ["HTTP_HOST"])

    environ['wsgi.charset'] = 'utf-8'
    url = environ["PATH_INFO"]
    #print "url: ", url
    #print "host: ", environ["HTTP_HOST"]
    if url[0:6] == "/html/":
        standart_response(start_response, "text/html")
        html = common.read_file_to_str(url[1:])
    elif url[0:4] == "/js/":
        standart_response(start_response, "text/javascript")
        html = common.read_file_to_str(url[1:])
    elif url[0:5] == "/css/":
        standart_response(start_response, "text/css")
        html = common.read_file_to_str(url[1:])
    elif url == "/yml.xml":
        standart_response(start_response, "text/xml")
        html = common.read_file_to_str(url[1:])
    elif url[0:9] == "/catalog/":
        standart_response(start_response, "text/html")
        html = scg.goods_main_view(url, "id")
    elif url[-6:] == "/goods":
        standart_response(start_response, "text/html")
        html = scg.goods_main_view(url)
    elif url == "/stat":
        standart_response(start_response, "text/html")
        html = scg.stat()
    elif url == "/":
        standart_response(start_response, "text/html")
        html = common.read_file_to_str("index.html")
    elif url[0:6] == "/libs/":
        standart_response(start_response, "text/javascript")
        html = common.read_file_to_str(url[1:])
    elif url == "/cart":
        standart_response(start_response, "text/html")
        html = common.read_file_to_str("html/cart.html")
    elif url[0:4] == "/ws/":
        standart_response(start_response, "application/json")
        html = make_json_ans( url, environ )
    elif url[0:7] == "/debug/":
        standart_response(start_response, "text/html")
        html = str(ret)
    
    if url[0:5] == "/png/":
        status = '200 OK'
        headers = [('Content-type', 'image/png')]
        start_response(status, headers)
        #ret = file(url[1:])
        ret = open(url[1:], "rb").read()
    elif url == "/favicon.ico":
        status = '200 OK'
        headers = [('Content-type', 'image/ico')]
        start_response(status, headers)
        ret = open(url[1:], "rb").read()
    else:
        ret = [common._U(html)]
    
    return ret

if __name__ == '__main__':
    from paste import httpserver
    from paste.exceptions import errormiddleware
    from paste import evalexception
    import datetime
    #app = errormiddleware.ErrorMiddleware(application, debug=True)
    app = evalexception.EvalException(application)
    #app = application
    #httpserver.serve(AuthDigestHandler(dump_environ, realm, authfunc), host='127.0.0.1', port='8080')
    print "Start at {date}".format(date = datetime.datetime.now())
    httpserver.serve(app, host = sett.host, port = sett.port)
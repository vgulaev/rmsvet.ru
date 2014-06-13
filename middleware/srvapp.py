def application(environ, start_response):
    status = '200 OK'
    output = 'Hello World my friend!'

#    response_headers = [('Content-type', 'text/plain'),
#                        ('Content-Length', str(len(output)))]
#    start_response(status, response_headers)
    headers = [('Content-type', 'text/plain')]

    start_response(status, headers)

    ret = ["%s: %s\n" % (key, value)
           for key, value in environ.iteritems()]
    #statistic.calls += 1
    #print "calls: " + str(statistic.calls)
    #return [output]
    return ret

    #return [output]
if __name__ == '__main__':
    from paste import httpserver
    httpserver.serve(application, host='127.0.0.1', port='8080')
from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

# A relatively simple WSGI application. It's going to print out the
# environment dictionary after being updated by setup_testing_defaults
class statistic(object):
	"""docstring for statistic"""
	calls = 0
	def __init__(self):
		self.arg = arg
		
def simple_app(environ, start_response):
    setup_testing_defaults(environ)

    status = '200 OK'
    headers = [('Content-type', 'text/plain')]

    start_response(status, headers)

    ret = ["%s: %s\n" % (key, value)
           for key, value in environ.iteritems()]
    statistic.calls += 1
    print "calls: " + str(statistic.calls)
    #return ret
    return "Hello word!!!"

httpd = make_server('', 8000, simple_app)
print "Serving on port 8000..."
httpd.serve_forever()
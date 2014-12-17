from http.server import BaseHTTPRequestHandler

class HTTPRequestHandler( BaseHTTPRequestHandler ):
    """docstring for HTTPRequestHandler"""
    def do_HEAD(s):
        pass
        """s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()"""
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        bs = bytes( '<html><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><head><title>Title goes here.</title></head>', "utf-8" )
        s.wfile.write( bs )
        bs = bytes( "<body><p>This is a test.</p>", "utf-8" )
        s.wfile.write( bs )
        bs = bytes( "<p>You accessed path: %s</p>" % s.path, "utf-8" )
        s.wfile.write( bs )
        bs = bytes( "<p>Вышла Маша по грибы</p>", "utf-8" )
        s.wfile.write( bs )
        bs = bytes( "</body></html>", "utf-8" )
        s.wfile.write( bs )
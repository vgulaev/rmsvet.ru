from http.server import BaseHTTPRequestHandler
import common

class HTTPRequestHandler( BaseHTTPRequestHandler ):
    """docstring for HTTPRequestHandler"""
    def ans_like_html( self ):
        pass
    def ans_like_404( self ):
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            bs = common.read_file_to_str( "html/404.html" )
            self.wfile.write( bs )
    def do_GET( self ):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            bs = common.read_file_to_str( "index.html" )
            self.wfile.write( bs )
        else:
            self.ans_like_404()

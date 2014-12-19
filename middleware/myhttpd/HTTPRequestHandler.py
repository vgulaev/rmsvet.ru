from http.server import BaseHTTPRequestHandler
import common
import json
import urllib.parse
import wsservers as ws
import staticcontentgenerator as scg
import os.path

class HTTPRequestHandler( BaseHTTPRequestHandler ):
    """docstring for HTTPRequestHandler"""
    def ans_like_text_file( self, filename, contenttype ):
            if os.path.isfile( filename ):
                self.send_response(200)
                self.send_header( "Content-type", contenttype )
                self.end_headers()
                bs = common.read_file_to_str( filename )
                self.wfile.write( bs )
            else:
                self.ans_like_404()
    def ans_like_text( self, html ):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            bs = bytearray( html, "utf-8" )
            self.wfile.write( bs )
    def ans_like_404( self ):
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            bs = common.read_file_to_str( "html/404.html" )
            self.wfile.write( bs )
    def do_POST( self ):
        if self.path == "/ws/ezsp-query":
            self.send_response(200)
            self.send_header( "Content-type", "application/json" )
            self.end_headers()
            length = int(self.headers['Content-Length'])
            post_data = urllib.parse.parse_qs( self.rfile.read( length ).decode( "utf-8" ) )
            ans = "{}"
            if self.path == "/ws/ezsp-query":
                eq = post_data[ "ezsp-query" ]
                ans = ws.ezspquery( eq[0] )
            bs = bytes( ans, "utf-8" )
            self.wfile.write( bs )
    def do_GET( self ):
        #print( self.path )
        if self.path == "/":
            self.ans_like_text_file( "index.html", "text/html" )
        elif self.path[ -5: ] == ".html":
            self.ans_like_text_file( "html/" + self.path[ 1: ], "text/html" )
        elif self.path[ -3: ] == ".js":
            self.ans_like_text_file( self.path[ 1: ], "text/javascript" )
        elif self.path[ -4: ] == ".css":
            self.ans_like_text_file( self.path[ 1: ], "text/css" )
        elif self.path[ -4: ] == ".ico":
            self.ans_like_text_file( self.path[ 1: ], "image/ico" )
        elif self.path[ -4: ] == ".png":
            self.ans_like_text_file( self.path[ 1: ], "image/png" )
        elif self.path[ -4: ] == ".xml":
            self.ans_like_text_file( self.path[ 1: ], "text/xml" )
        elif self.path[0:9] == "/catalog/":
            html = scg.goods_main_view( self.path, "id" )
            self.ans_like_text( html )
        elif self.path[ -6: ] == "/goods":
            html = scg.goods_main_view( self.path )
            self.ans_like_text( html )
        elif self.path[0:10] == "/site-map/":
            html = scg.make_map( self.path[10:] )
            self.ans_like_text( html )
        else:
            self.ans_like_404()
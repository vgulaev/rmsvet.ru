from http.server import BaseHTTPRequestHandler
import common
import json
import urllib.parse
import time
import wsservers as ws
import sett
import staticcontentgenerator as scg
import os.path

class HTTPRequestHandler( BaseHTTPRequestHandler ):
    """docstring for HTTPRequestHandler"""
    def ans_like_text_file( self, filename, contenttype ):
            if os.path.isfile( filename ):
                self.send_response(200)
                self.send_header( "Content-type", contenttype )
                exptime = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime( time.time() + 60 * 60 ) )
                self.send_header( "expires", exptime )
                self.send_header( "cache-control", "public, max-age=86400" )
                self.send_header( "Last-Modified", common.env[ "HTTP-Modified-Since" ] )
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
    def ans_like_304( self ):
            self.send_response(304)
            self.send_header( "Last-Modified", common.env[ "HTTP-Modified-Since" ] )
            self.end_headers()
    def ans_like_404( self ):
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            bs = common.read_file_to_str( "html/404.html" )
            self.wfile.write( bs )
    def get_postdata( self ):
        self.send_response(200)
        self.send_header( "Content-type", "application/json" )
        self.end_headers()
        length = int( self.headers[ "Content-Length" ] )
        res = urllib.parse.parse_qs( self.rfile.read( length ).decode( "utf-8" ) )
        return res
    def do_POST( self ):
        ans = "{}"
        if self.path == "/ws/ezsp-query":
            post_data = self.get_postdata()
            eq = post_data[ "ezsp-query" ]
            ans = ws.ezspquery( eq[0] )
            bs = bytes( ans, "utf-8" )
            self.wfile.write( bs )
        elif self.path == "/ws/write-order-to-srv":
            post_data = self.get_postdata()
            ans = ws.create_order( post_data[ "data" ][ 0 ] )
            bs = bytes( ans, "utf-8" )
            self.wfile.write( bs )
    def do_GET( self ):
        o = urllib.parse.urlparse( self.path )
        path = o.path
        ms = self.headers[ "If-Modified-Since" ]
        if sett.server_dep != "windows dev":
            if ms is not None:
                tm = time.mktime( time.strptime( ms, '%a, %d %b %Y %H:%M:%S GMT' ) )
                if tm >= common.env[ "Modified-Since" ]:
                    self.ans_like_304( )
                    return
        if path == "/":
            self.ans_like_text_file( "html/index.html", "text/html" )
        elif path[ -5: ] == ".html":
            self.ans_like_text_file( "html/" + path[ 1: ], "text/html" )
        elif path[ -3: ] == ".js":
            self.ans_like_text_file( path[ 1: ], "text/javascript" )
        elif path[ -4: ] == ".css":
            self.ans_like_text_file( path[ 1: ], "text/css" )
        elif path[ -4: ] == ".ico":
            self.ans_like_text_file( path[ 1: ], "image/ico" )
        elif path[ -4: ] == ".png":
            self.ans_like_text_file( path[ 1: ], "image/png" )
        elif path[ -4: ] == ".svg":
            self.ans_like_text_file( path[ 1: ], "image/svg+xml" )
        elif path[ -4: ] == ".xml":
            self.ans_like_text_file( path[ 1: ], "text/xml" )
        elif path[ -4: ] == ".otf":
            self.ans_like_text_file( path[ 1: ], "font/opentype" )
        elif path[0:9] == "/catalog/":
            html = scg.goods_main_view( path, "id" )
            self.ans_like_text( html )
        elif path[ -6: ] == "/goods":
            html = scg.goods_main_view( path )
            if html == False:
                self.ans_like_404()
            else:
                self.ans_like_text( html )
        elif path[ 0 : 8 ] == "/orders/":
            html = scg.orders( path[ 8: ] )
            self.ans_like_text( html )
        elif path[ 0 : 14 ] == "/getorderspdf/":
            filename = scg.getorderspdf( path[ 14: ] )
            self.ans_like_text_file( "out.pdf", """application/pdf;filename="out.pdf" """)
            #self.ans_like_text( html )
        elif path[0:10] == "/site-map/":
            html = scg.make_map( path[ 10: ] )
            if html == False:
                self.ans_like_404()
            else:
                self.ans_like_text( html )
        elif path == "/stat":
            html = scg.stat()
            self.ans_like_text( html )
        else:
            self.ans_like_404()
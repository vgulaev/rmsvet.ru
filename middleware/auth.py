import dbclasses.dbworker
import common
import time

def baseauth(self, login, password):
    sql = """SELECT * FROM users WHERE (username = '{0}' and userpassword = '{1}');""".format(login, password)
    cursor = (dbclasses.dbworker.getcon()).cursor()
    cursor.execute( sql )
    sql = cursor._rows
    if len( sql ) > 0:
        s_id = 2398132790147809
        self.send_response(200)
        self.send_header( "Content-type", "text/html" )
        exptime = time.strftime( '%a, %d %b %Y %H:%M:%S GMT', time.gmtime( time.time() + 60 * 60 ) )
        self.send_header( "expires", exptime )
        self.send_header( "cache-control", "public, max-age=86400" )
        self.send_header( "Last-Modified", common.env[ "HTTP-Modified-Since" ] )
        self.send_header( "Set-Cookie",
        """{0};
        expires=Tue, 19 Jan 2038 03:14:07 GMT;
        path=/""".format( s_id ) )
        self.end_headers()
        bs = common.read_file_to_str( "html/index.html" )
        self.wfile.write( bs )
        addfld = dbclasses.dbobj.objects["sessions"]()
        addfld.session = s_id
        addfld.username = login
        addfld.write()
        return True
    else:
        return False

def auth(s_id):
    sql = """SELECT * FROM sessions WHERE sessions.session = '{0}';""".format(s_id)
    cursor = (dbclasses.dbworker.getcon()).cursor()
    cursor.execute( sql )
    sql = cursor._rows
    if len( sql ) > 0:
        return True
    else:
        return False

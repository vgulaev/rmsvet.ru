# -*- coding: utf-8 -*-
import codecs
import time
import os

import dbclasses.dbobj
import dbclasses.dbworker

def detect_common_env( domain = "ezsp.ru" ):
    d = dbclasses.dbobj.objects[ "domains" ]()
    if d.find( caption = domain ):
        o = dbclasses.dbobj.objects[ "organization" ]( )
        if o.find( id = d.organization ):
            env[ "organization" ] = o
    fname = "PRICE_1C.XLS"
    if os.path.isfile( fname ):
        tm = time.gmtime( os.path.getmtime( fname ) )
    else:
        tm = time.gmtime( time.time() )
    env[ "Modified-Since" ] = time.mktime( tm )
    env[ "HTTP-Modified-Since" ] = time.strftime('%a, %d %b %Y %H:%M:%S GMT', tm )
    env[ "price_count" ] = 0
    con = dbclasses.dbworker.getcon()
    cursor = con.cursor()
    sql = "select count(*) from prices"
    cursor.execute( sql )
    row = cursor.fetchone()
    if row is not None:
        env[ "price_count" ] = row[ 0 ]

def _D( s ):
    ret = dict( s )
    for ( key, val ) in s.items():
        if isinstance( val, unicode ):
            ret[ key ] = s[ key ].encode("utf-8")
    return ret

def _U(s):
    res = s
    if isinstance(s, unicode):
        res = s.encode("utf-8")
    return res
        
def _Q(s):
    return "'{s}'".format(s = s)

def read_file_to_str(filename):
    t = open( filename, "rb" )
    #t = codecs.open(filename, encoding="utf-8")
    return t.read()

def price_maker( val ):
    ret = 0
    if val != 0:
        newprice = round(val, -2) - 1
        if abs(newprice - val) / val < 0.02:
            ret = newprice
        else:
            newprice = round(val, -1) - 0.11
            if (newprice - val) / val < 0.02:
                ret = newprice
            else:
                ret = val
    
    return "{0:.2f}".format(ret)

def fetch_to_row_dict( cursor ):
    res = []
    row = cursor.fetchone()
    row_index = 1
    while row is not None:
        r = {}
        for (i, e) in enumerate( row ):
            r[ cursor.description[i][0] ] = e
        r[ "index" ] = row_index
        row_index += 1
        res += [ r ]
        row = cursor.fetchone()
    return res

env = { "organization" : None, "Modified-Since" : None }
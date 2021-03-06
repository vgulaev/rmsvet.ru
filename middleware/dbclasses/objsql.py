# -*- coding: utf-8 -*-
from .propdict import propdict

class objsql():
    def addprop( self, pdict ):
        self.prop += [ pdict ]
    def __init__( self, pname, pprop, ptables = [], powner = None ):
        self.istable = not(powner == None)
        self.prop = []
        self.tables = []
        if self.istable:
            self.name = powner + "_" + pname
            self.addprop( pdict = propdict( pname = "count", ptype = "INT" ) )
        else:
            self.name = pname
        self.attname = pname
        self.addprop( pdict = propdict( pname = "id", ptype = "VARCHAR(36)" ) )
        for e in pprop:
            self.addprop( pdict = e )
        for e in ptables:
            self.tables += [e]
        self.sqlwrite = self.getsqlwrite()
    def keysforsql( self ):
        res = ",".join( [ e["name"] for e in self.prop ] )
        return res
    def valuesforsql( self ):
        res = ",".join( [ "%({e})s".format( e = e["name"] ) for e in self.prop ] )
        return res
    def updateforsql( self ):
        res = ",".join( [ "{e}=%({e})s".format( e = e["name"] )  for e in self.prop ] )
        return res
    def getsqlwrite( self ):
        sql = "INSERT INTO `{tn}` ({keys}) VALUES ({values})".format( tn = self.name, keys = self.keysforsql(), values = self.valuesforsql() )
        sql += "ON DUPLICATE KEY UPDATE {eq}".format( eq = self.updateforsql() )
        return sql
    def sqlcreate( self ):
        sql = "CREATE TABLE IF NOT EXISTS `{tname}` (".format( tname = self.name )
        sqllines = []
        for e in self.prop:
            tp = e["type"]
            if tp[0:4] == "own:":
                tp = "VARCHAR(36)"
            sqll = "{name} {type}".format( name = e["name"], type = tp )
            #if e["name"] == "id":
                #sqll += " PRIMARY KEY"
            sqllines += [sqll]
        if self.istable:
            sqllines += [ "primary key ( id, count )" ]
        else:
            sqllines += [ "primary key ( id )" ]
        sql += ", ".join(sqllines) + ") ENGINE=INNODB CHARACTER SET utf8;"
        return sql
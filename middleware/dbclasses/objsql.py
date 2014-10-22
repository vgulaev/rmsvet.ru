# -*- coding: utf-8 -*-
from propdict import propdict

class objsql():
    def addprop( self, pdict ):
        self.prop += [ pdict ]
    def __init__( self, pname, pprop, ptables = None ):
        self.name = pname
        self.prop = []
        self.tables = []
        self.addprop( pdict = propdict( pname = "id", ptype = "CHAR(36)" ) )
        for e in pprop:
            self.addprop( pdict = e )
    def sqlcreate( self ):
        sql = "CREATE TABLE IF NOT EXISTS `{tname}` (".format( tname = self.name )
        sqllines = []
        for e in self.prop:
            tp = e["type"]
            if tp[0:4] == "own:":
                tp = "CHAR(36)"
            sqll = "{name} {type}".format( name = e["name"], type = tp )            
            if e["name"] == "id":
                sqll += " PRIMARY KEY"
            sqllines += [sqll]
        sql += ", ".join(sqllines) + ") ENGINE=INNODB CHARACTER SET utf8 COLLATE utf8_bin;"
        return sql
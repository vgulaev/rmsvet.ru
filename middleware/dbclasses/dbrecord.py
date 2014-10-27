# -*- coding: utf-8 -*-
import dbworker
import uuid

class dbrecord():
    def __init__( self ):
        pass
    def write( self ):
        sql = self.__mtdata__.sqlwrite
        db = dbworker.getcon()
        cursor = db.cursor()
        if self.id == "":
            self.id = str(uuid.uuid1())
        d = {}
        for e in self.__mtdata__.prop:
            d[ e["name"] ] = getattr( self, e["name"] )
        cursor.execute( sql, d )
        db.commit()
        for e in self.__mtdata__.tables:
            tbl = getattr(self, e.attname)
            tbl.write()
        return True
    def find( self, *args, **kwargs ):
        pass
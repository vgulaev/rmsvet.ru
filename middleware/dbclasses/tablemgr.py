# -*- coding: utf-8 -*-
import dbworker
class tablemgr():
    def add( self ):
        ref = {}
        self.row += [ref]
        ref["id"] = self.owner.id
        ref["count"] = len( self.row ) - 1
        return ref
    def __init__( self, powner = None, pmtdata = None ):
        self.__mtdata__ = pmtdata
        self.owner = powner
        self.row = []
    def write( self ):
        db = dbworker.getcon()
        cursor = db.cursor()
        for e in self.row:
            #print e
            cursor.execute( self.__mtdata__.sqlwrite, e )
            db.commit()
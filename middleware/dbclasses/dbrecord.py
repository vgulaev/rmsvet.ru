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
        res = False
        sql = "SELECT * FROM {tn}"
        sql = sql.format(tn = self.__mtdata__.name)
        if len(kwargs) > 0:
            sql += " where ";
            sql += " and ".join("{e} = %({e})s".format( e = e ) for e in kwargs)
            ds = dict()
            for e in kwargs:
                ds[str(e)] = kwargs[e]
            db = dbworker.getcon()
            cursor = db.cursor()
            cursor.execute( sql,ds )
            row = cursor.fetchone()
            if row is not None:
                for ( i,e ) in enumerate(row):
                    setattr( self, cursor.description[i][0], e )
                res = True
        return res
    """def __setitem__( self, key, value ):
        setattr( self, key, value )
    def __getitem__( self, name ):
        return getattr( self, name )"""
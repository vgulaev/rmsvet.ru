# -*- coding: utf-8 -*-
from . import dbschema
from .dbrecord import dbrecord
from .tablemgr import tablemgr

def create_class_for_table( schema_class ):
    class retclass( dbrecord ):
        def __init__( self ):
            for e in self.__mtdata__.prop:
                setattr( self, e["name"], "" )
            for e in self.__mtdata__.tables:
                setattr( self, e.attname, tablemgr( powner = self, pmtdata = e ) )
    retclass.__mtdata__ = schema_class
    return retclass

objects = {}
for e in dbschema.schema["objects"]:    
    objects[e.name] = create_class_for_table( e )
    for t in e.tables:
        objects[t.name] = create_class_for_table( t )
# -*- coding: utf-8 -*-
import dbschema
import dbrecord
objects = {}
for e in dbschema.schema["objects"]:
    class retclass( dbrecord.dbrecord ):
        def __init__( self ):
            for e in self.__mtdata__.prop:
                setattr(self, e["name"], "")
    retclass.__mtdata__ = e
    
    objects[e.name] = retclass
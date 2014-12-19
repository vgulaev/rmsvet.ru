# -*- coding: utf-8 -*-
from . import dbworker
from . import dbschema
def droptable( tname ):
    sql = "DROP TABLE IF EXISTS `{tn}`".format( tn = tname )
    db = dbworker.getcon()
    cursor = db.cursor()
    cursor.execute( sql )
    cursor.close()
def dropall():
    db = dbworker.getcon()
    cursor = db.cursor()
    sql = "show TABLES"
    cursor.execute( sql )
    row = cursor.fetchone()
    while row is not None:
        droptable( row[0] )
        row = cursor.fetchone()
def createtable():
    for e in dbschema.schema["objects"]:
        sql = e.sqlcreate()
        db = dbworker.getcon()
        cursor = db.cursor()
        cursor.execute( sql )
        for t in e.tables:
            sql = t.sqlcreate()
            db = dbworker.getcon()
            cursor = db.cursor()
            cursor.execute( sql )
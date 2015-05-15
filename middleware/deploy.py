# -*- coding: utf-8 -*-
import pymysql as MySQLdb
import dbclasses.dbmaintenance
import dbclasses.dbworker
import sett
import dbclasses.dbobj
from checon import PyLibCC
from checon import JSLibCC
from checon import CheColl
"""
Connection on DataBase
"""
dbclasses.dbworker.cred = dbclasses.dbworker.loadmysqlcredential( sett )
def get_db_connection():
    cred = dbclasses.dbworker.cred
    db = MySQLdb.connect(host = cred["host"], user = cred["user"], passwd = cred["passwd"], charset = 'utf8')
    return db
"""
Check library and charset UTF-8
"""
PyLibCC.CheckInstModD(r"..//middleware")
JSLibCC.CheckInstModD(r"..//middleware")
sql = """SHOW VARIABLES LIKE 'character_sets_dir';"""
db = get_db_connection()
cursor = db.cursor()
cursor.execute( sql )
print(cursor._rows[0][1])
CheColl.CheColl(r"{0}".format(cursor._rows[0][1])+"Index.xml")
"""
Check exist vg_site_db
"""
sql = """SHOW DATABASES;"""
cursor.execute( sql )
exist = False
for i in cursor._rows:
    if i[0] == "vg_site_db":
        exist = True
        break

if exist:
    """
    Delete the vg_site_db
    """
    sql = "DROP DATABASE vg_site_db"
    cursor.execute( sql )
    db.commit()
    print( "DB droped" )
else:
    """
    Create the vg_site_db
    """
    sql = "CREATE DATABASE IF NOT EXISTS vg_site_db"
    cursor.execute(sql)
    db.commit()
    dbclasses.dbmaintenance.createtable()
    print( "DB preparation complate" )
    p = dbclasses.dbobj.objects[ "partners" ]()
    p.caption = "OCS"
    p.catalog_name = "catalog_ocs"
    p.write()
    o = dbclasses.dbobj.objects[ "organization" ]()
    o.caption = "ezsp"
    o.write()
    p = dbclasses.dbobj.objects[ "domains" ]()
    p.organization = o.id
    p.caption = "ezsp.ru"
    p.write()
    p = dbclasses.dbobj.objects[ "domains" ]()
    p.organization = o.id
    p.caption = "eazyshop.ru"
    p.write()
    p = dbclasses.dbobj.objects[ "domains" ]()
    p.organization = o.id
    p.caption = "127.0.0.1:8080"
    p.write()
    o = dbclasses.dbobj.objects[ "organization" ]()
    o.caption = "rmsvet"
    o.write()
    p = dbclasses.dbobj.objects[ "domains" ]()
    p.organization = o.id
    p.caption = "rmsvet.ru"
    p.write()
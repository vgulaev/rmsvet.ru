# -*- coding: utf-8 -*-
import MySQLdb
import re
import uuid
from web.db import __repr__

class field_type:
    reference = 0
    decimal = 1
    char = 2
    null = 3
    
def loadmysqlcredential():
    passwd = ""
    r = {   "host" : 'localhost',
            "user" : 'root',
            "passwd" : passwd}
    return r

class dbrecord(object):
    direct_assign = ["type", "maxlength", "precision", "val", "__fields__",
                     "__name__", "__owner__"]
    def __init__(self, val = "", fld_type = None, owner = None, name = ""):
        #self.__db__ = ""
        if not hasattr(self, "__fields__"):
            self.__fields__ = []
        #self.__fields_type__ = []
        if (fld_type == None):
            self.type = field_type.reference
        else:
            if type(fld_type) == unicode:
                self.__owner__ = owner
                self.__name__ = name
                if fld_type.find(u"char") > -1:
                    self.type = field_type.char
                    m = re.search(r"\(([A-Za-z0-9_]+)\)", fld_type)
                    self.maxlength = int(m.group(1))
                    self.val = ""
                elif fld_type.find(u"decimal") > -1:
                    self.type = field_type.decimal
                    m = re.search(r"\(([A-Za-z0-9_(,)]+)\)", fld_type)
                    len_and_pre = (m.group(1)).split(",")                    
                    self.precision = int(len_and_pre[1])
                    self.val = 0
    def char_to_str(self):
        return self.val[:self.maxlength]
    def dec_to_str(self):
        return str(round(self.val, self.precision))
        #return str(round(self.val))
    def __str__(self):
        res = object.__str__(self)
        if self.type == field_type.char:
            res = self.char_to_str()
        elif self.type == field_type.decimal:
            res = self.dec_to_str()
        return res
    def str_to_db(self):
        res = str(self)
        if (self.type == field_type.char):
            res = "'{s}'".format(s = res)
        return res
    #__repr__ = __str__
    def __getitem__(self, key):
        return getattr(self, key)
    def new_id(self):
        self.val = str(uuid.uuid1())
    def is_null(self):
        res = False
        if (self.val == 0 or self.val == ""):
            res = True
        return res
    def write(self):
        if self.id.is_null():
            self.id.new_id()
        sql = "INSERT INTO {tn} ({keys}) VALUES ({values})";
        keys = ",".join(self.__fields__ )
        values = ",".join(self[e].str_to_db() for (e, t) in zip(self.__fields__, self.__fields_type__))
        sql = sql.format(tn = self.__tablename__, keys = keys, values = values)
        sql += " ON DUPLICATE KEY UPDATE {eq}".format(eq = self.fl_for_dup_key())
        #print sql
        self.__db__.cursor.execute(sql)
        self.__db__.db.commit()
    def drop(self):
        sql = "DROP TABLE IF EXISTS {tn}".format(tn = self.__tablename__)
        self.__db__.cursor.execute(sql)
        print sql
    def fl_for_dup_key(self):
        l = [e + " = " + self[e].str_to_db() for (e, t) in zip(self.__fields__, self.__fields_type__) if e != "id"]
        return ",".join(l)
    def __getattr___(self, name):
        #print "try get"
        return object.__getattribute__(self, name)
        #return self.__dict__[name]
    __getattribute__ = __getattr___
    def __setattr__(self, name, val):
        #self.__dict__[name] = val
        if isinstance(val, dbrecord):
            self.__dict__[name] = val
        else:
            #direct_assign = ((name == "type") or (name == "maxlength"))
            if name in dbrecord.direct_assign:
                self.__dict__[name] = val
            elif name in self.__fields__:
                self[name].val = val
        #print "try set"""
    #__repr__ = __str__
class dbworker:
    def __init__(self):
        cred = loadmysqlcredential()
        self.db = MySQLdb.connect(host = cred["host"], user = cred["user"], passwd = cred["passwd"], db = "vg_site_db", charset = 'utf8')
        self.cursor = self.db.cursor()
    def create_table(self):
        sql = [
        """
        CREATE TABLE IF NOT EXISTS goods (
        id CHAR(36) PRIMARY KEY,
        caption CHAR(100) COLLATE utf8_general_ci,
        price DECIMAL(8,2)
        ) ENGINE=INNODB CHARACTER SET utf8 COLLATE utf8_bin;
        """]
        for e in sql:
            self.cursor.execute(e)
            self.db.commit()
    def class_from_table(self, table_name):
        sql = "show columns from {tn}".format(tn = table_name)
        self.cursor.execute(sql)
        
        retclass = dbrecord()
        #print retclass.__dict__
        class retclass(dbrecord):
            def __init__(self):
                dbrecord.__init__(self)
                for (e,t) in zip(self.__fields__, self.__fields_type__):
                    self.__dict__[e] = dbrecord(fld_type = t, owner = self, name = e)
        #retclass.__init__()
        retclass.__db__ = self;
        retclass.__fields__ = []
        retclass.__fields_type__ = []
        retclass.__tablename__ = table_name
        row = self.cursor.fetchone()
        while row is not None:
            retclass.__fields__ += [row[0]]
            retclass.__fields_type__ += [row[1]]
            dbr = dbrecord(fld_type = row[1])
            #setattr(retclass, row[0], dbr)
            row =  self.cursor.fetchone()
        return retclass
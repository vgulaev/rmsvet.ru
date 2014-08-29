import MySQLdb

def loadmysqlcredential():
    passwd = ""
    r = {   "host" : 'localhost',
            "user" : 'root',
            "passwd" : passwd}
    return r

def fl_to_str(v, t):
    if (t.find("decimal") > -1):
        res = "1.33"
    else:
        res = "'{v}'".format(v = v)
    return res

class dbrecord:
    def __init__(self):
        __db__ = ""
        __fields__ = []
        __fields_type__ = []
    def __getitem__(self, key):
        return getattr(self, key)
    def write(self):
        sql = "INSERT INTO {tn} ({keys}) VALUES ({values})";
        keys = ",".join(self.__fields__ )
        values = ",".join(fl_to_str(self[e], t) for (e, t) in zip(self.__fields__, self.__fields_type__))
        sql = sql.format(tn = self.__tablename__, keys = keys, values = values)
        #sql += " ON DUPLICATE KEY UPDATE {eq}".format(eq = self.fl_for_dup_key())
        #print sql
        self.__db__.cursor.execute(sql)
        self.__db__.db.commit()
    def fl_for_dup_key(self):
        return ""

class dbworker:
    def __init__(self):
        cred = loadmysqlcredential()
        self.db = MySQLdb.connect(host = cred["host"], user = cred["user"], passwd = cred["passwd"], db = "vg_site_db", charset = 'utf8')
        self.cursor = self.db.cursor()
    def create_table(self):
        sql = """
        CREATE TABLE goods (
        id CHAR(36) PRIMARY KEY,
        caption CHAR(100),
        price DECIMAL(8,2)
        ) ENGINE=INNODB CHARACTER SET utf8 COLLATE utf8_bin;
        """
        self.cursor.execute(sql)
        self.db.commit()
    def class_from_table(self, table_name):
        sql = "show columns from {tn}".format(tn = table_name)
        self.cursor.execute(sql)
        
        class retclass(dbrecord):
            pass
        retclass.__db__ = self;
        retclass.__fields__ = []
        retclass.__fields_type__ = []
        retclass.__tablename__ = table_name
        row = self.cursor.fetchone()
        while row is not None:
            retclass.__fields__ += [row[0]]
            retclass.__fields_type__ += [row[1]]
            setattr(retclass, row[0], "")
            row =  self.cursor.fetchone()
        return retclass

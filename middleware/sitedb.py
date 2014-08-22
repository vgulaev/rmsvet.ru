import MySQLdb

def loadmysqlcredential():
    passwd = ""
    r = {   "host" : 'localhost',
            "user" : 'root',
            "passwd" : passwd}
    return r

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
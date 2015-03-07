import dbclasses.dbworker
import dbclasses.sqlresulttable
import codecs
import sett

dbclasses.dbworker.cred = dbclasses.dbworker.loadmysqlcredential( sett )

def table_to_file():
    con = dbclasses.dbworker.getcon()
    cursor = con.cursor()
    sql = "select * from prices INTO OUTFILE 'c:/my.csv'"
    cursor.execute( sql )

def create_big_data():
    f = codecs.open( "my.csv", "w", "utf-8" )
    for i in range( 500000 ):
        f.write( str( i ) + "\tname\turl\t\t273000.00\t" + str( i ) + "\t0.00\t\tf6483265-c425-11e4-9616-4ceb421a4969\tfrom 1c\t1\n" )

def clear_table():
    con = dbclasses.dbworker.getcon()
    cursor = con.cursor()
    sql = "delete from prices where id <> '000'"
    cursor.execute( sql )
    con.commit()

def load_from_file_to_db():
    con = dbclasses.dbworker.getcon()
    cursor = con.cursor()
    sql = "LOAD DATA INFILE 'c:/Users/Valentin/workspace/rmsvet.ru/middleware/my.csv' INTO TABLE prices"
    cursor.execute( sql )
    con.commit()

#create_big_data()
clear_table()
#load_from_file_to_db()

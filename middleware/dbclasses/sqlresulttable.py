import pymysql
#from pymysql.constants import FieldType

class sqlresulttable( object ):
    def load_from_cursor( self, ones ):
        desc = ones.description
        print( desc ) 
        row = ones.fetchone()
        while row is not None:
            self.rows += [ [ e for e in row ] ]
            row = ones.fetchone()
    def __init__( self, ones ):
        self.columns = []
        self.rows = []
        if isinstance( ones, pymysql.cursors.Cursor ):
            self.load_from_cursor( ones )

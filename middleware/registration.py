import dbclasses.dbworker

def registration(login, password):
    sql = """SELECT * FROM users WHERE username = '{0}';""".format(login)
    cursor = (dbclasses.dbworker.getcon()).cursor()
    cursor.execute( sql )
    sql = cursor._rows
    if len( sql ) > 0:
        return False
    else:
        addfld = dbclasses.dbobj.objects["users"]()
        addfld.username = login
        addfld.userpassword = password
        addfld.write()
        return True

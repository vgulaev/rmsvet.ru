1. For correct collation have to prepare the add string for "Index.xml" (http://dev.mysql.com/doc/refman/5.7/en/adding-collation.html). utf8_general_ci_eng_cy
2. Have to move standart js libs from middleware/libs
3. For correct work we need sett.py file. The simple sett.py:

    >>> #clent enviroment
    >>> server_dep = "windows dev"
    >>> #password for correct MySQL link
    >>> mysql_pass = ""
    >>> #trivial for correct web app
    >>> host = "127.0.0.1"
    >>> port=8080

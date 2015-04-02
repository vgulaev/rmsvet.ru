from os import path
from checon import FilePath

def OpenFile( pathD, set ):
    allF = FilePath( pathD )
    for file in allF:
        if len( set ) != 0:
            nameF, ext = path.splitext( file )
            if ext.lower( ) in set:
                workF = open( path.abspath( file ), encoding = "utf-8" )
                notInStr = True
                strType = 0
                for str in workF:
                    for chr in str:
                        if (chr == "'") or (chr == '"'):
                            if (chr == "'") and notInStr:
                                notInStr = False
                                strType = 1
                            elif (chr == '"') and notInStr:
                                notInStr = False
                                strType = 2
                            if (chr == "'") and strType == 1:
                                notInStr = True
                                strType = 0
                            else:
                                notInStr = True
                                strType = 0
                        else:
                            if not notInStr:
                                continue
                            if chr in ("+", "-", "*", "/", "<", ">", "=",)
                            ... А если это += -= >= <= == и тд.... что же делать....

OpenFile( r"C:\Users\movis08\Desktop\checon", (".py", ".html") )
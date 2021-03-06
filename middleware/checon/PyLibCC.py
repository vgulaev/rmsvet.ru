# -*- coding: utf-8 -*-
"""
Checking module connection libraries and modules Python 3.4
"""

from os import walk
from os import path

"""
Function to simplify.
"""

"""
Function return path to all file in dir.
"""
def FilePath(dir):
    m = set()
    for i,j,k in walk(dir):
        for a in k:
            m.add("{0}//{1}".format(i,a))
    return m

"""
Function to find the first word in the line.
A word is a set of characters enclosed in any - any of the following entities (start line, end of line, space).
"""
def FirstWord(str):
    length = len(str)
    res = []
    res.append("")
    for i in range(length):
        if str[i] != " ":
            for j in range(i, length):
                if str[j] != " ":
                    res[0] += str[j].replace('\n','')
                else:
                    res.append(j+1)
                    break
            break
    return res

"""
Basic functions.
"""

"""
Finding function libraries and module in "*.py" files.
"""

def FindModF( file ):
    mods = set()
    nameF, ext = path.splitext( file )
    if ext.lower() == ".py":
        f = open( path.abspath( file ), encoding = "utf-8" )
        for line in f:
            length = len( line )
            if line != "":
                if length >= 8:
                    if FirstWord(line.lower())[0] == "import":
                        mods.add((line.replace('\n',''), file))
                    elif FirstWord(line.lower())[0] == "from":
                        mods.add((line.replace('\n',''), file))
                elif length >= 6:
                    if FirstWord(line.lower())[0] == "from":
                        mods.add((line.replace('\n',''), file))
        return mods
    else:
        return mods

"""
Finding function libraries and module in all "*.py" files for this folder.
"""

def CheckInstModD(dir):
    m = set()
    for i in FilePath(dir):
        m.update(FindModF(i))
    k=CheckInstMod(m)
    print(len(m))
    print(len(k[1]))
    print(len(k[2]))

"""
Check function using libraries and modules for operation. Return mods in string, massive used and unused mods and libraries.
"""
def CheckInstMod( mods ):
    used = set( )
    unused = set( )
    for str in mods:
        try:
            exec( str[0] )
            used.add( str )
        except:
            try:
                eval( str[0] )
                used.add( str )
            except:
                if str[0].find("from") >= 0: #Это строка с from?
                    if (str[0][5:str[0].find("import")]).find(".") > 0: #Модуль формата чтото.чтото?
                        module = (str[0][5:str[0].find("import")])[:(str[0][5:str[0].find("import")]).find(".")]
                    else: #Модуль формата чтото
                        module = (str[0][5:str[0].find("import")].strip(".")).strip(" ")
                        #Не работает в случае когда модуль находится в той же папке что и файл который его использует.
                else: #Значит с import
                    if str[0][7:].find(".") > 0: #Модуль формата чтото.чтото?
                        module = (str[0][7:])[:str[0][7:].find(".")]
                    else: #Модуль формата чтото
                        module = ( str[0][7:] )
                if path.exists(path.normpath(path.join(path.dirname(str[1]), module))) or path.exists(path.normpath(path.join(path.dirname(str[1]), module + '.py'))): #Файл или папка существуют?
                    used.add( str )
                else:
                    unused.add( str )
                    print( r"The line '{0}' contains unsupported library".format( str ) )
    use = [ ]
    use.append( mods )
    use.append( used )
    use.append( unused )
    return use

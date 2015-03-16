"""
Checking module connection libraries and modules Python 3.4
"""

import os.path as path

"""
Function to simplify.
"""

"""
Function to find the first word in the line.
A word is a set of characters enclosed in any - any of the following suschnosti (start line, end of line, space).
"""
def FirstWord(str):
    length = len(str)
    res = ""
    for i in range(length):
        if str[i] != " ":
            for j in range(i, length):
                if str[j] != " ":
                    res += str[j].replace('\n','')
                else: break
            break
    return res

"""
Basic functions.
"""

"""
Finding function libraries and module in "*.py" files.
"""

def FindModF( file ):
    if file[ len(file)-3: ].lower() == ".py":
        f = open( path.abspath( file ), encoding = "utf-8" )
        mods = set()
        cont = 0
        for line in f:
            length = len( line )
            if line != "":
                if length >= 8:
                    if FirstWord(line.lower()) == "import":
                        mods.add(line)
                    elif FirstWord(line.lower()) == "from":
                        mods.add(line)
                elif length >= 6:
                    if FirstWord(line.lower()) == "from":
                        mods.add(line)
        for i in mods:
            print ( i )
        return mods
    else: print("It is no Python 3.4 files")

"""
Finding function libraries and module in all "*.py" files for this folder.
"""

#def FindModD():
#    pass

"""
Check function using libraries and modules for operation.
"""
def CheckInstMod( mods ):
    for i in mods:
        try:
            #str ='import {0}'.format( i )
            #exec( str )
            exec( i )
            print("Line '{0}' can be used".format( i ))
        except:
            print("The line '{0}' contains unsupported library".format( i ))

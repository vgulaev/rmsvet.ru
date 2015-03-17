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
            m.add("{0}\\{1}".format(i,a))
    return m

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
    mods = set()
    if file[ len(file)-3: ].lower() == ".py":
        f = open( path.abspath( file ), encoding = "utf-8" )
        cont = 0
        for line in f:
            length = len( line )
            if line != "":
                if length >= 8:
                    if FirstWord(line.lower()) == "import":
                        mods.add((line.replace('\n',''), file))
                    elif FirstWord(line.lower()) == "from":
                        mods.add((line.replace('\n',''), file))
                elif length >= 6:
                    if FirstWord(line.lower()) == "from":
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
#   for i in m:
#       print(i)
    print(len(m))
    print(len(k[1]))
    print(len(k[2]))

"""
Check function using libraries and modules for operation. Return mods in string, massive used and unused mods and libraries.
"""
def CheckInstMod( mods ):
    used = set()
    unused = set()
    for str in mods:
        try:
            compile(str[0], str[1], 'exec')
            used.add(str)
#            print("Line '{0}' can be used".format( str ))
        except:
            try:
                compile(str[0], str[1], 'eval')
                used.add(str)
#               print("Line '{0}' can be used".format( str ))
            except:
                unused.add(str)
                print("The line '{0}' contains unsupported library".format( str ))
    use = []
    use.append(mods)
    use.append(used)
    use.append(unused)
    return use
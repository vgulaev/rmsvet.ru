"""
Checking module connection libraries and modules JavaScript
"""

from .PyLibCC import FilePath as fp
from .PyLibCC import FirstWord as fw
from os import path

"""
Basic function
"""

"""
Finding function libraries and module in "*.py" files.
"""

def FindModF( file ):
    mods = set()
    ras=file[ len(file)-5: ].lower()
    if ras == ".html" or ras == ".mako":
        f = open( path.abspath( file ), encoding = "utf-8" )
        for line in f:
            line1 = line.replace('\n','')
            line1 = line1.replace('\t','')
            length = len( line1 )
            if line1 != "":
                if length >= 22:
                    if fw(line1.lower()) == "<script":
                        mods.add((line1, file))
        return mods
    else:
        return mods

"""
Check function using libraries and modules for operation. Return mods in string, massive used and unused mods and libraries.
"""
def CheckInstMod( mods ):
    used = set()
    unused = set()
    for str in mods:
        length = len(str[0])
        mod=""
        b = False
        for i in range(11,length):
            if b:
                break
            if (str[0])[i-5:i]=='src="':
                for j in range(i, length):
                    if str[0][j]!='"':
                        mod += str[0][j]
                    else:
                        b = True
                        break
        if compile("""import execjs
execjs.eval(import {0})""".format(mod[1:]),str[1],'exec'):
            used.add(mod)
        else:
            unused.add(mod)
    use = []
    use.append(mods)
    use.append(used)
    use.append(unused)
    return use

"""
Finding function libraries and module in all "*.py" files for this folder.
"""

def CheckInstModD(dir):
    m = set()
    files = fp(dir)
    for i in files:
        m.update(FindModF(i))
    k=CheckInstMod(m)
#   for i in m:
#       print(i)
    print(len(m))
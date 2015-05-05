# -*- coding: utf-8 -*-
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
Finding function JavaScript libraries and module in "*.html" and "*.mako" files.
"""

def FindModF( file ):
    mods = set()
    nameF, ext = path.splitext( file )
    ras = ext.lower()
    if ras == ".html" or ras == ".mako":
        f = open( path.abspath( file ), encoding = "utf-8" )
        for line in f:
            line1 = line.replace('\n','')
            line1 = line1.replace('\t','')
            length = len( line1 )
            if line1 != "":
                if length >= 22:
                    word = fw(line1.lower())
                    if word[0] == "<script":
                        if fw(line1.lower()[word[1]:])[0][:4] == "src=":
                            mods.add((line1, file))
        return mods
    else:
        return mods

"""
Check function using libraries and modules for operation. Return mods in string, massive used and unused mods and libraries.
"""
def CheckInstMod( mods, dir ):
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
        if path.exists(path.normpath(dir+mod)):
            used.add((mod, str[1]))
        elif path.exists(path.normpath(path.join(path.dirname(str[1]), mod))):
            used.add((mod, str[1]))
        else:
            unused.add((mod, str[1]))
            print(r"The line '{0}' have unsupported library".format( str ))
    use = []
    use.append(mods)
    use.append(used)
    use.append(unused)
    return use

"""
Finding function libraries and module in all "*.html" and "*.mako' files for this folder.
"""

def CheckInstModD(dir):
    m = set()
    files = fp(dir)
    for i in files:
        m.update(FindModF(i))
    k=CheckInstMod(m, path.abspath(dir))
    print(len(m))
    print(len(k[1]))
    print(len(k[2]))

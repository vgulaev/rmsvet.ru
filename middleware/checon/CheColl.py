# -*- coding: utf-8 -*-
from os import path
import codecs

def CheColl(index):
    if path.exists(index):
        bool1 = True
        a = []
        a.append(0)
        flag = '0'
        file = codecs.open(index, "r", "utf-8" )
        linesA = file.readlines()
        for nStr in range(len(linesA)):
            madeStr = (((linesA[nStr].strip(" ")).strip('\t')).strip('\n')).strip('\r')
            if bool1:
                if madeStr == r'<charset name="utf8">':
                    bool1 = False
                    flag = '1'
                    a.append(nStr)
            if not bool1:
                if madeStr == r'<collation name="utf8_general_ci_eng_cy" id="1033">':
                    flag = '2'
                    a.append(nStr)
                    break
                elif madeStr == r'</charset>':
                    a.append(nStr)
                    break
        if flag == '0':
            print( r'<charset name="utf8"> is not exist' )
        elif flag == '1':
            print( r'<collation name="utf8_general_ci_eng_cy" id="1033"> is not exist' )
        elif flag == '2':
            print( r'<charset name="utf8"> and <collation name="utf8_general_ci_eng_cy" id="1033"> is exist' )
        if flag == '1':
            middleware = path.normpath(path.join(path.dirname(__file__), r'../'))
            exec(compile(open(middleware + r'/make_collation_file.py', "rb").read(), middleware + r'/make_collation_file.py', 'exec'))
            b = codecs.open( middleware + r'/collation.xml', "r", "utf-8" )
            linesB = b.readlines()
            for nStr in range(len(linesB)):
                linesA.insert(a[2]+nStr, linesB[nStr])
            linesA.insert(a[2]+len(linesB), "\n")
            file = codecs.open(index, "w", "utf-8" )
            file.writelines(linesA)
    else:
        print(r"file {0} is not exist".format(index))

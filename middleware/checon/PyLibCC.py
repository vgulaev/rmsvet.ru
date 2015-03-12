"""
Модуль проверки используемых библиотек Python3.4
"""

import os.path as path

"""
Функции необходимые для упрощения написания основных функций
"""

"""
Функция для нахождения первого слова в строке. Словом считается набор символов заключенный в
каких - либо следующих сущьностях (Начало строки, Конец строки, пробел)
"""
def FirstWord(str):
    length = len(str)
    res = ""
    for i in range(length):
        if str[i] != " ":
            for j in range(i, length):
                if str[j] != " ":
                    res += str[j]
                else: break
            break
    return res

"""
Основные функции
"""

"""
Функция просмотра используемых библиотек, для файлов *.py которые подаются при
вызове этой функции.
"""

"""
Пока что не работает в таких случаях:
1) Если присутствует "as" и после него идет еще какая-нибудь библиотека
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
                    if line[ 0: 6 ].lower() == "import":
                        mods.add(line)
                        """for i in range( 6, length ):
                            if cont > 0:
                                cont -= 1
                                continue
                            if line[ i ] !=" ":
                                res = FirstWord( line[i:] )
                                if res[ len(res)-1 ] == ",":
                                    cont = len( res )
                                    res = res[ :-1 ]
                                    mods.add( res.strip( "\n" ) )
                                else:
                                    mods.add( res.strip( "\n" ) )
                                    break"""
                    elif line[ 0: 4 ].lower() == "from":
                        mods.add(line)
                        """for i in range( 4, length ):
                            if cont > 0:
                                cont -= 1
                                continue
                            if line[ i ] !=" ":
                                res = FirstWord( line[i:] )
                                if res[ len(res)-1 ] == ",":
                                    res = res[ :-1 ]
                                    mods.add( res.strip( "\n" ) )
                                    cont = len( res )
                                else:
                                    mods.add( res.strip( "\n" ) )
                                    break"""
                elif length >= 6:
                    if line[ 0: 4 ].lower() == "from":
                        mods.add(line)
                        """for i in range( 4, length ):
                            if line[ i ] !=" ":
                                res = FirstWord( line[i:] )
                                if res[ len(res)-1 ] == ",":
                                    i += len( res )
                                    res = res[ :-1 ]
                                    mods.add( res.strip( "\n" ) )
                                else:
                                    mods.add( res.strip( "\n" ) )
                                    break"""
        for i in mods:
            print ( i )
        return mods
    else: print("Этот файл не является файлом Python 3.4")

"""
Функция просмотра используемых библиотек, для файлов *.py которые находятся в
папке адрес которой подается при вызове этой функции.
"""

"""
Функция проверки работоспособности библиотек (вывод функций: FindModD, FindModF)
"""
def CheckInstMod( mods ):
    for i in mods:
        try:
            #str ='import {0}'.format( i )
            #exec( str )
            exec( i )
            print("Строка {0} может быть исполнена".format( i ))
        except:
            print("В строке {0} присутствуют неподдерживаемые библиотеки".format( i ))

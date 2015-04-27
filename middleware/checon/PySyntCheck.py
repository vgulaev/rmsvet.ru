from os import path
from .PyLibCC import FilePath
import codecs

def OpenFile( pathD, set, center = {"+", "-", "*", "/", "<", ">", "="}, left = {"(","[","{"}, right = {")","]","}"}, warning = {"+=","-=","/=","*=",">=","<=","<>","><","=="}):#подаем директорию и множество форматов файлов
    center = center
    warning = warning
    left = left
    right = right
    allF = FilePath( pathD)#нашли все файлы в дирректориии и поддерикториях
    for file in allF:#проходимся по ним
        if len( set ) != 0:#если множество форматов не пусто, то....
            nameF, ext = path.splitext( file )#разобьем путь к файлу на пару путь с названием и формат
            if ext.lower( ) in set:#проверим есть ли вормат в множестве форматов, если да, то....
                workF = codecs.open( path.abspath( file ), "rw", "utf-8" )#откроем файл
                notInStr = True#отметим то, что мы не в строке ("", '')
                strType = 0#Зададим тип строки (скольки кавычная строка)))
                for str in workF:#Проходимся по строкам файла
                    for nChr in range(len(str)):#Проходимся по символам строки
                        chr = str[nChr]#рассматриваемый сейчас символ
                        if (chr == "'") or (chr == '"'):#символ начала или конца строки? Если да, то....
                            if (chr == "'") and notInStr:#Зашли в строку из 1 кавычки?
                                notInStr = False
                                strType = 1
                            elif (chr == '"') and notInStr:#Зашли в строку из 2 кавычек?
                                notInStr = False
                                strType = 2
                            if (chr == "'") and strType == 1:#Вышли из строки из 1 кавычки
                                notInStr = True
                                strType = 0
                            else:#Вышли из строки из 2 кавычек
                                notInStr = True
                                strType = 0
                        else:#если это не символ начала, конца строки, то....
                            if not notInStr:#Мы находимся в строке?
                                continue#Тогда смотри следующий символ
                            if chr in left:#это левый символ? тогда....
                                if str[nChr-1] == " ":#если прошлый пробел, то удалить его
                                    Удалили, а индекс то сменился.... И что делать? Символ проскочили....

OpenFile( r"C:\Users\movis08\Desktop\checon", (".py", ".html") )
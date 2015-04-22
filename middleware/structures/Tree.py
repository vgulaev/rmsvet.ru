# -*- coding: utf-8 -*-

class CatalogTree():
    """
    Class constructor
    """
    def __init__(self, Parent = "", CID = "", CN = "", Level = 0):
        self.ParentLink = ""
        self.Child = []
        self.ParentCategoryID = Parent
        self.CategoryID = CID
        self.CategoryName = CN
        self.NestingLevel = Level
        self.flag1 = True
    """
    Work with childs
    """
    def addChild(self, ParentID = CategoryID, CID = "", CN = ""):
        child = CatalogTree(ParentID, CID, CN, self.NestingLevel +1)
        child.ParentLink = self
        self.Child.append(child)
    def delChild(self, string = "", variant = 0):
        for i in range(len (self.Child)):
            if self.Child[i].CategoryID == string:
                if variant == 0:
                    self.Child.clear()
                elif variant == 1:
                    self.Child[i].__del__()
                    break
                elif variant == 2:
                    for j in range(len(self.Child[i].Child)):
                        self.Child[i].Child[j].ParentLink = self
                        self.Child[i].Child[j].NestingLevel -= 1
                    self.Child += self.Child[i].Child
                    self.Child.pop(i)
                    break

if __name__ == '__main__':
    a = CatalogTree()
    a.addChild(CID="1", CN = "asd")
    a.addChild(CID="2", CN = "asf")
    a.addChild(CID="3", CN = "asg")
    b=a.Child[2]
    b.addChild(CID="5", CN="qwe")
    a.delChild("3",2)
    b=3+3
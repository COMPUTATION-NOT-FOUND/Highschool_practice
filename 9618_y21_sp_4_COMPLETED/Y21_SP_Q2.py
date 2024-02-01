class hiddenbox:
    def __init__(self,boxname,creator,datehidden,gamelocation):
        self.__boxname=boxname
        self.__creator=creator
        self.__datehidden=datehidden
        self.__gamelocation=gamelocation
        self.__lastfinds=[[None for i in range (2)]for j in range (10)]
        self.__active="inactive"

    def getgamelocation(self):
        return self.gamelocation
    def boxname(self):
        return self.boxname



TheBoxes=[hiddenbox("","","","") for  k in range(10000)]


def newbox():
    global TheBoxes
    Name=input("input name : ")
    creator=input("input creator : ")
    datehidden=input("input date hidden : ")
    gamelocation=input("input game location :")
    TheBoxes.append(hiddenbox(Name,creator,datehidden,gamelocation))

newbox()


class puzzlebox(hiddenbox):
    def __init__(self, boxname, creator, datehidden, gamelocation,puzzlebox,solution):
        super().__init__(boxname,creator,datehidden,gamelocation)
        self.__puzzlebox=puzzlebox
        self.__solution=solution



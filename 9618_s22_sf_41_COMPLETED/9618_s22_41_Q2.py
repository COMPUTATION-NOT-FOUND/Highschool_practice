# Write your code here :-)
class balloon:
    def __init__(self,colour,defenseitem):
        self.__colour=colour
        self.__defenseitem=defenseitem
        self.__health=100

    def getdefenseitem(self):
        return(self.__defenseitem)

    def gethealth(self):
        return(self.__health)

    def changehealth(self,P):
        self.__health-=P

    def checkhealth(self):
        if self.__health<1:
            return True
        else:
            return False


defenseinput=input("please enter a defense item :")
colourinput=input("please enter a baloon colour: ")

balloon1=balloon(colourinput,defenseinput)

def defend(Myballoon):
    strength=int(input("input intger strength of attack"))
    Myballoon.changehealth(strength)
    print("ballon defend with", Myballoon.getdefenseitem())
    if Myballoon.checkhealth()==False:
        print("balloon survives")
    else:
        print("no health left")

    return Myballoon


defend(balloon1)







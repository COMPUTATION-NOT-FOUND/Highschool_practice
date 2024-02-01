# Write your code here :-)
"""
CLASS card
    DECLARE Number :INTEGER
    DECLARE Colour :STRING
END CLASS
"""
class card:
    def __init__(self,Number,Colour):
        self.__Number=Number
        self.__Colour=Colour
    def GetNumber(self):
         return(self.__Number)



    def GetColour(self):
        return(self.__Colour)

Red1=card(1,"red")
Red2=card(2,"red")
Red3=card(3,"red")
Red4=card(4,"red")
Red5=card(5,"red")
Blue1=card(1,"blue")
Blue2=card(2,"blue")
Blue3=card(3,"blue")
Blue4=card(4,"blue")
Blue5=card(5,"blue")
yellow1=card(1,"yellow")
yellow2=card(2,"yellow")
yellow3=card(3,"yellow")
yellow4=card(4,"yellow")
yellow5=card(5,"yellow")

"""
CLASS HAND
    DECLARE Cards: Array[0:9] of card
    DECLARE firstcard : Integer
    DECLARE numbercards: Integer
END CLASS
"""
class Hand:
    def __init__(self,c1,c2,c3,c4,c5):
        self.__Cards=[c1,c2,c3,c4,c5]
        for J in range (5):
            self.__Cards.append(card(0,0))
        self.__fristcard=0
        self.__Numbercards=5
    def getcard(self,index):
        return(self.__Cards[index])

Player1=Hand(Red1,Red2,Red3,Red4,yellow1)
Player2=Hand(yellow2,yellow3,yellow4,yellow5,Blue1)

def calculatevalue(player):
    points=0
    for i in range (5):
        if str((player.getcard(i)).GetColour()) == "red":
            points=points+5
        if str((player.getcard(i)).GetColour()) == "blue" :
            points+=10
        if  str((player.getcard(i)).GetColour()) == "yellow" :
            points+=5
    return points



score1=calculatevalue(Player1)
score2=calculatevalue(Player2)

if score1 == score2:
    print("match is  draw")
elif score1> score2:
    print("match won by player1")
else:
    print("match won by player 2")








# Write your code here :-)
class card:
    def __init__(self,colour,number):
        self.__colour=colour
        self.__number=number

    def getcolour(self):
        return(self.__colour)

    def getnumber(self):
        return(self.__number)



cards=[None for i in range(30)]

filename = "CardValues.txt"
f=open(filename,"rt")
for j in range (30):
    number=f.readline().strip()
    colour=f.readline().strip()
    cards[j]=card(colour,number)

print(str(cards[1].getcolour()))


cardchosen=[None for j in range(30)]


def choosecard():
    global cardchosen
    chosen=False
    y=int(input( "numbers from 1 to 30 "))
    if y>=1 and y<=30:
        if cardchosen[y-1]!= None :
            chosen=True
    while y<1 or y>30  or chosen ==True:
        print("inavlid input try again")
        y=int(input( "numbers from 1 to 30 "))
        if y>=1 and y<=30:
            if cardchosen[y-1]!= None:
                chosen=True
    cardchosen[y-1]="taken"
    return y-1

player1=[]
for l in range(4):
    returnedcard=choosecard()
    player1.append(cards[returnedcard])
for k in range(4):
    print(str(player1[k].getcolour()))
    print(str(player1[k].getnumber()))

















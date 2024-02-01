class Character:
    """
    Private name as string
    Private xcoordinate as integer
    private Y coordinate as integer
    """
    def __init__(self,name ,xcoordinate,ycoordinate):
        self.__name=name
        self.__xcoordinate=xcoordinate
        self.__ycoordinate=ycoordinate

    def getname(self):
        return(self.__name)

    def getxcoordinate(self):
        return(self.__xcoordinate)

    def getycoordinate(self):
        return(self.__ycoordinate)

    def changecoordinates(self,xchange,ychange):
        self.__xcoordinate+=xchange
        self.__ycoordinate+=ychange



characters=[]

f=open("characters.txt","rt")
for i in range(10):
    name = f.readline().strip().lower()
    xcoordinate = int(f.readline().strip())
    ycoordinate = int(f.readline().strip())
    characters.append(Character(name,xcoordinate,ycoordinate))

search=(input("input charcater for search").lower())
flag=False
while flag==False:
    for j in range (10):
        if search==str(characters[j].getname()):
            index=j
            flag=True
    if flag == False:
        print("name not present")
        search = (input("input charcater for search")).lower()


flag2=False
while flag2==False :
    movement = (input("eneter A,W,S,D to move").upper())
    if movement == 'A':
        flag2 = True
    elif movement == 'w':
        flag2 = True
    elif movement == 's':
        flag2 = True
    elif movement == 'D':
        flag2 = True
    else:
        flag2= False




if movement=='A':
    characters[j].changecoordinates(-1,0)
elif movement == 'S':
    characters[j].changecoordinates(0,-1)
elif movement == 'W':
    characters[j].changecoordinates(0,1)
elif movement == 'D':
    characters[j].changecoordinates(1,0)

print(str(characters[j].getname()),"has changed positions to x=" , str(characters[j].getxcoordinate()),'and y=' ,str(characters[j].getycoordinate()))













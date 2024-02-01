# Write your code here :-)
class picture:
    def __init__(self,descriptionp,widthp,heightp,framecolourp):
        self.__description=descriptionp
        self.__width=widthp
        self.__height=heightp
        self.__framecolour=framecolourp
    def getdescription(self):
        return(self.__description)
    def getwidth(self):
        return(self.__width)
    def getheight(self):
        return(self.__height)
    def getframecolour(self):
        return(self.__framecolour)
    def setdescription(self,newdescription):
        self.__description=newdescription

picturearray=[]
for i in range (100):
    picturearray.append(picture("",0,0,""))

def readdata(picturearray):
    filename="Pictures.txt"
    counter=0
    try:
        file=open(filename,"rt")
        description=((file.readline()).strip()).lower()
        while description!="":

            width=int((file.readline()).strip())
            height=int((file.readline()).strip())
            framecolour=(file.readline()).strip().lower()
            picturearray[counter]=picture(description,width,height,framecolour)

            description=(file.readline()).strip().lower()
            counter+=1
        file.close
    except IOError:
        print("error file couldnt be found")
    return counter,picturearray

numberofpictures,picturearray=readdata(picturearray)

print(numberofpictures)

framecolour=(input("framecolour: ")).lower()
maxwidth=int(input("input max width: "))
maxheight=int(input("input max height: "))

for z in range (numberofpictures):
    if picturearray[z].getframecolour()==framecolour:
        if (picturearray[z].getwidth() <= maxwidth):
            if (picturearray[z].getheight() <= maxheight):
                print(str(picturearray[z].getdescription()), " " , str(picturearray[z].getwidth()), " ", str(picturearray[z].getheight()))

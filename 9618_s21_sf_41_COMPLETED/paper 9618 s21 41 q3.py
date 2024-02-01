#paper 9618 s21 41
#Q3
class treasurechest:
    def __init__(self,question,answer,point):
        self. __question=question
        self. __answer=answer
        self. __point=point
    def getquestion(self):
        return self. __question
    def getpoints(self,attemptno):
        if attemptno==1:
            return self. __point
        elif attemptno==2:
            return (self. __point/2)
        elif attemptno==3 or attemptno==4:
            return (self. __point/4)
        else:
            return 0


    def checkanswer(self,answer):
       flag=False
       if int(answer)==int(self.__answer):
            flag=True
       return flag
arraytreasure=[]
def readdata():
    global arraytreasure
    try:
        f=open("treasurechestdata.txt","rt")
    except:
        print("file not found")
    for i in range (5):
        question=f.readline()
        answer=f.readline()
        point=f.readline()
        arraytreasure.append(treasurechest(question,answer,point))
readdata()

x=int(input("input question number 1 to 5: "))
print(arraytreasure[x].getquestion())
answer=input("input answer: ")
print(arraytreasure[x].checkanswer(answer))
noattempts=1
arraytreasure[x].checkanswer(answer)
while arraytreasure[x].checkanswer(answer)==False:
    print(arraytreasure[x].getquestion())
    answer=input("input answer")
    print(arraytreasure[x].checkanswer(answer))
    noattempts+=1
    arraytreasure[x].checkanswer(answer)
print("points awarded",arraytreasure[x].getpoints(noattempts))

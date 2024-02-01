TheData=[20,3,4,8,12,99,4,26,4]

def insertionsort(TheData):
    for i in range (9):
        Datatoinsert=TheData[i]
        inserted=0
        nextvalue=i-1
        while nextvalue>=0 and inserted!=1:
            if Datatoinsert < TheData[nextvalue]:
                TheData[nextvalue+1]=TheData[nextvalue]
                nextvalue-=1
                TheData[nextvalue+1]=Datatoinsert
            else:
                inserted=1

def printarray(TheData):
    for i in range(len(TheData)):
        print(TheData[i])

print("before sorrting")
printarray(TheData)

insertionsort(TheData)
print("after sorting")
printarray(TheData)


def find():
    global TheData
    x=int(input("enter a number to be found"))
    found=False
    for i in range (len(TheData)):
        if TheData[i]==x:
            found=True
    if found==True:
        print("found")
        return True
    else:
        print("not found")
        return False


find()
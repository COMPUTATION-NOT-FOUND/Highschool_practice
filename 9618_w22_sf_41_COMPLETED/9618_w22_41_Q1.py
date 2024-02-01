dataarray=[0 for i in range (100)]
def readfile():
    global dataarray
    try:
        textfile="IntegerData.Txt"
        file=open(textfile,'rt')
        for x in range(0,100):
            buffer=file.readline()
            buffer=int(buffer.strip())
            dataarray[x]=buffer

    except IOError:
        print("couldn't find this file")
readfile()
print(dataarray)

def findvalues():
    count=0
    numtosearch=int(input("enter num to search"))
    for j in range (100):
        if dataarray[j]==numtosearch:
            count+=1
    return count


counts=findvalues()
print(counts)


def bubblesort():
    total=len(dataarray)-1
    print(total)
    swap= True
    while swap == True and total >0 :
        swap=False
        for k in range (total):
            if dataarray[k]>dataarray[k+1]:
                temp=dataarray[k]
                dataarray[k]=dataarray[k+1]
                dataarray[k+1]=temp
                swap=True
        total-=1



bubblesort()
print(dataarray)





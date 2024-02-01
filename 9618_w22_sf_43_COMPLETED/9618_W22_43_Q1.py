
global DataArray

DataArray=[None for i in range (100)]

def ReadFile():
    try:
        file=open("IntegerData.Txt","rt")
        for j in range (100):
            DataArray[j]=int((file.readline()).strip())


    except IOError:
        print("file doesnt exist")
def FindValues():
    NumForSearch=int(input("enter value to be serached :"))
    while NumForSearch<1 or NumForSearch>100:
        NumForSearch=int(Input("enter value to be serached"))
    count=0
    for k in range (100):
        if DataArray[k] == NumForSearch:
            count+=1
    return count



ReadFile()
print (" the number of time the integer appears in the array",FindValues())

def bubblesort():
    sort=True
    totalsorts=len(DataArray)
    while sort == True:
        sort=False
        totalsorts-=1
        for l in range (totalsorts):
            if DataArray[l] >  DataArray[l+1]:
                temp1=DataArray[l]
                DataArray[l]=DataArray[l+1]
                DataArray[l+1]=temp1
                sort=True

bubblesort()
print(DataArray)









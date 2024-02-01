# Write your code here :-)
dataarray=[2,6,7,9,10,1,3,4,5,8]
def bubblesort():
    total=len(dataarray)-1
    print(total)
    swap= True
    while swap == True and total >=0 :
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

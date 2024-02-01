# Write your code here :-)


import random

arraydata=[[-1 for i in range (10)]for j in range (10)]

for i in range(10):
    for l in range (10):
        arraydata[i][l]=random.randint(1,100)
        arraydata[i][l]=random.randint(1,100)


arraylength=10

for x in range(arraylength):
    for y in range(arraylength -1):
        for z in range(arraylength -y -1):
            if arraydata[x][z]>arraydata[x][z+1]:
                tempvalue=arraydata[x][z]
                arraydata[x][z]=arraydata[x][z+1]
                arraydata[x][z+ 1]=tempvalue


def printarray():
    for i in range (10):
        for j in range (10):
            print(arraydata[i][j], " ", end="")
        print("")

printarray()

def binarysearch(searcharray,lower,upper,searchvalue):
    if upper >= lower:
        mid=(lower+(upper-1))//2
        if searcharray[0][mid]==searchvalue:
            return Mid
        elif searcharray[0][mid]>searchvalue:
            return binarysearch(searcharray,lower,mid-1,searchvalue)
        elif searcharray[0][mid]<searchvalue:
            return binarysearch(searcharray,mid+1 ,upper ,searchvalue)
    return -1




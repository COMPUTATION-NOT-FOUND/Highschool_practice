#paper 9618 s21 41
#Q2 a
arraydata=[10,5,6,7,1,12,13,15,21,8]
#Q2 b
def linearsearch(number):
    flag=False
    for i in range (9) :
        if arraydata[i]== number:
            flag=True
    return flag

#Q2 b ii
number=int(input("input number to be searched: "))
if linearsearch(number)==True:
    print("number is present in the array")
else:
    print("number is not present in the array")
#Q2 c
def bubblesort(arraydata):
    for x in range (9):
        for y in range(8):
            if arraydata[y] < arraydata[y+1]:
                temp=arraydata[y+1]
                arraydata[y+1]=arraydata[y]
                arraydata[y]=temp


#just for checking
print(arraydata)

for i in range (9):
    print(str(arraydata[i]))

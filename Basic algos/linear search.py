numbers=[1,2,3,4,5,6,7]
item=4
index=0
found=False
upperbound=len(numbers)
while index<upperbound and found==False:
    if numbers[index]==item:
        print("item found at:",index)
        found=True
    else:
        index+=1


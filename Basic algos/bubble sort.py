numbers=[1,2,3,4,5,6,7]
swap=True
upperbound=len(numbers)-1

while swap or upperbound>0:
    swap=False
    for index in range(upperbound):
        if numbers[index]<numbers[index+1]:
            temp=numbers[index]
            numbers[index]=numbers[index+1]
            numbers[index+1]=temp
            swap=True
    upperbound= upperbound-1
print(numbers)



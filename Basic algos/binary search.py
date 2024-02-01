numbers=[1,2,3,4,5,6,7]
upperbound= len(numbers) -1
lowerbound=0

item=4
found=False

while not found and lowerbound <= upperbound:
    index =(upperbound + lowerbound)//2
    if numbers[index]==item:
        found=True
        print("item found at:",index)
    if item> numbers[index]:
        lowerbound= index+1
    if item < numbers[index]:
        upperbound =index-1
if not found:
    print(-1)





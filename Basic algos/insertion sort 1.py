numbers=[1,2,3,4,5,6,7]

for ptr in range(1,len(numbers)):
    for comp_ptr in range (0,ptr):
        if numbers[ptr]>numbers[comp_ptr]:
            temp=numbers[ptr]
            for i in range (ptr,comp_ptr,-1):
                numbers[i]=numbers[i-1]
            numbers[comp_ptr]=temp
print(numbers)


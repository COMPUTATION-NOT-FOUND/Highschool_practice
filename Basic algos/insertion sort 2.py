numbers=[1,2,3,7,5,4,6]

for ptr in range(1,7):
    temp=numbers[ptr]
    comp_ptr=ptr-1
    while numbers[comp_ptr]<temp and comp_ptr>-1:
        numbers[comp_ptr+1]=numbers[comp_ptr]
        comp_ptr-=1
    numbers[comp_ptr+1]=temp
print(numbers)


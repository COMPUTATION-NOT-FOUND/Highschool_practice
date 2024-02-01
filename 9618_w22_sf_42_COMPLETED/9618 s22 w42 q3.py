Queue=[-1 for i in range(100)]
tailpointer=0
headpointer=-1

print(Queue)

def Enqueue(Data):
    global tailpointer , headpointer
    if tailpointer < 101:
        if headpointer==-1:
            headpointer+=1
        Queue[tailpointer]=Data
        tailpointer+=1
        return True
    else:
        return False

for i in range(20):
    x=int(input("input number to add to the queue"))
    flag=Enqueue(x)
if flag == False:
    print("unsuccessful")
else:
    print("successful")

def recursiveoutput(start):
    if start==0:
         return Queue[start]
    else:
         return Queue[start] + recursiveoutput(start-1)


print(Queue)
y=recursiveoutput(tailpointer-1)
print(y)

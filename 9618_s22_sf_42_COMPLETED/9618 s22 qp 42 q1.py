global StackData
global stackpointer
StackData=[0,0,0,0,0,0,0,0,0,0]
stackpointer=0

def printstack():
    global StackData,stackpointer
    print(stackpointer)
    for i in range (0,10):
        print(StackData[i], end=(" "))

def push(number):
    global stackpointer
    flag=False
    if stackpointer<10:
        StackData[stackpointer]=number
        print("number successfully added to the stack")
        stackpointer+=1
        flag=True
    else:
        print("number not added to the stack")
    return print(flag)
for x in range (10):
    push(input("enter number pls :"))



def pop():
    global stackpointer
    if stackpointer==0:
        print("stack is empty")
    else:
        temp=stackpointer-1
        print(StackData[stackpointer-1])
        StackData[stackpointer-1]=0
        stackpointer-=1
printstack()
for x in range(2):
    pop()
printstack()



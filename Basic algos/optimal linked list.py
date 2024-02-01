freepointer=0
startpointer=-1


class node():
    def __init__(self,data,pointer):
        self.data=data
        self.pointer=pointer

def intialize(N):
    global linklist
    linklist=[]
    for i in range (N) :
        linklist.append(node(0,i+1))
    linklist[N-1]=node(0,-1)

def push(M):
    global linklist, freepointer, startpointer, Numberofitems
    if freepointer == -1:
        print("List is full")
    elif startpointer!=-1:
        nodepointer = freepointer
        freepointer = linklist[nodepointer].pointer
        linklist[nodepointer] =node(M,-1)
        previouspointer=startpointer
        while  linklist[previouspointer].pointer !=-1:
            previouspointer = linklist[previouspointer].pointer
        linklist[previouspointer].pointer=nodepointer

    else:
        nodepointer=freepointer
        startpointer= freepointer
        freepointer = linklist[nodepointer].pointer
        linklist[nodepointer] = node(M, -1)


def pull(x):
    global  freepointer,startpointer
    nodepointer=startpointer
    previouspointer=startpointer
    while linklist[nodepointer].data!= x and nodepointer!=-1:
        previouspointer=nodepointer
        nodepointer=linklist [nodepointer] .pointer

    """
    while linklist[previouspointer].pointer!=nodepointer:
        previouspointer=linklist[previouspointer].pointer
    """



    if nodepointer==startpointer:
        linklist[startpointer] .data =0
        startpointer=linklist[startpointer] .pointer
        linklist [nodepointer].pointer =freepointer
        freepointer=nodepointer
    elif nodepointer==  -1:
        print("data doesnt exist in the list")

    else:
        linklist[nodepointer].data=0
        linklist[previouspointer].pointer=linklist[nodepointer].pointer
        linklist[nodepointer].pointer=freepointer
        freepointer=nodepointer


def printll():
    for o in range (len(linklist)):
        print(linklist[o].data,linklist[o].pointer)
    print('freepointer',freepointer,'startpointer',startpointer)


intialize(10)

for l in range(6):
    x=input("number to store")
    push(int(x))

printll()

pull(5)
printll()

push(10)
printll()

pull(1)

printll()


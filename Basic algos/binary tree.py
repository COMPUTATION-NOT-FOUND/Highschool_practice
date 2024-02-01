rootpointer=0
numberofitems=0
order=[]
class node():
    def __init__(self):
        self.leftpointer=-1
        self.rightpointer=-1
        self.data=-1

def intialize(N):
    global bt
    bt=[]
    for i in range (N):
        bt.append(node())

def add(N):
    global rootpointer , numberofitems, bt

    if numberofitems !=(len(bt)) :

        if numberofitems != 0 :
            nodepointer=rootpointer


            """
            while nodepointer != numberofitems -1 :
                while bt[nodepointer].data > N and bt[nodepointer].leftpointer != -1 :
                    nodepointer=bt[nodepointer].leftpointer
                while bt[nodepointer].data <N and bt[nodepointer].rightpointer != -1:
                    nodepointer=bt[nodepointer].rightpointer


            """
            while bt[nodepointer].data > N and bt[nodepointer].leftpointer != -1 :
                nodepointer=bt[nodepointer].leftpointer
                while bt[nodepointer].data <N and bt[nodepointer].rightpointer != -1:
                    nodepointer=bt[nodepointer].rightpointer

            while bt[nodepointer].data <N and bt[nodepointer].rightpointer != -1:
                nodepointer=bt[nodepointer].rightpointer
                while bt[nodepointer].data > N and bt[nodepointer].leftpointer != -1 :
                    nodepointer=bt[nodepointer].leftpointer




            if bt[nodepointer].data > N:
                bt[numberofitems].data=N
                bt[nodepointer].leftpointer=numberofitems
                numberofitems+=1
            elif  bt[nodepointer].data < N:
                bt[numberofitems].data=N
                bt[nodepointer].rightpointer=numberofitems
                numberofitems+=1

        else:
            bt[rootpointer].data=N
            numberofitems+=1
    else:
        print("array is full create new array and transfer")



def printbt():
    for j in range (len(bt)):
        print( "leftpointer", bt[j].leftpointer , "rightpointer", bt[j].rightpointer,"data", bt[j].data)

def postorder(rootnode):
    if bt[rootnode].leftpointer !=-1:
        postorder(bt[rootnode].leftpointer)
    print(bt[rootnode].data)
    if bt[rootnode].rightpointer!=-1:
        postorder(bt[rootnode].rightpointer)






intialize(5)

for k in range(len(bt)):
    x=input("enter value to insert")
    add(int(x))

printbt()

postorder(rootpointer)














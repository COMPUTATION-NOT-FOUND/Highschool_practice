# Write your code here :-)
queuearray=[None for i in range (10)]
headpointer=0
tailpointer=0
numberofitem=0

def enqueue(queuearray,headpointer,tailpointer,numberofitem,datatoadd):
    if numberofitem==10:
        return False,queuearray,headpointer,tailpointer,numberofitem

    queuearray[tailpointer]=datatoadd

    if tailpointer>=9:
        tailpointer=0
    else:
        tailpointer=tailpointer+1

    numberofitem+=1

    return True,queuearray,headpointer,tailpointer,numberofitem

def dequeue(queuearray,headpointer,numberofitem):
    returnvalue=""
    if numberofitem==0:
        return "false",queuearray,headpointer,numberofitem
    else:
        returnvalue=queuearray[headpointer]
        queuearray[headpointer]=None
        headpointer+=1
        if headpointer>9 :
            headpointer=0
        numberofitem-=1
        return returnvalue,queuearray,headpointer,numberofitem
"""

def Dequeue(Queue, Head, Tail, NumItems):
    if NumItems == 0:
        return (false, Queue, Head, Tail, NumItems)
    else:
        ReturnValue = Queue[Head]
        Head = Head + 1
        if Head >= 9:
            Head = 0
        NumItems = NumItems - 1
        return(ReturnValue, Queue, Head, Tail, NumItems)
"""

for count in range (11):
    datatoadd=input("data to add :")
    flag,queuearray,headpointer,tailpointer,numberofitem= enqueue(queuearray,headpointer,tailpointer,numberofitem,datatoadd,)
    if flag==False:
        print("data not successfully added")

print(numberofitem)


print(queuearray)

for k in range (10):
    printvalue=""
    printvalue,queuearray,headpointer,numberofitem=dequeue(queuearray,headpointer,numberofitem)
    print(printvalue)

print(queuearray)









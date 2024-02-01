# paper 9618 s21 qp 41
#Q1 a
class node:
    def __init__(self,data,nextnode):
        self.data=data
        self.nextnode=nextnode

#Q1 b
linklist=[node(1,1),node(5,4),node(6,7),node(7,-1) ,node(2,2) , node(0,6) , node(0,8) , node(56,3) , node(0,9) , node(0,-1)]
l=linklist
startpointer=0
emptylist=5
#Q1 c i, ii
def outputnodes (linklist,startpointer):
    currentpointer=startpointer
    while currentpointer != -1:
        print (str(linklist[currentpointer].data))
        currentpointer=linklist[currentpointer].nextnode
outputnodes ( linklist,startpointer)
#Q1 d
def addnode(linklist,emptylist,startpointer):
    currentpointer=startpointer
    while linklist[currentpointer].nextnode != -1:
        currentpointer=linklist[currentpointer].nextnode
    flag=False
    if emptylist!= -1:
        linklist[emptylist].data=input("insert data to be added to link list: ")
        linklist[currentpointer].nextnode=emptylist
        nextfreeptr=linklist[emptylist].nextnode
        linklist[emptylist].nextnode=-1
        emptylist=nextfreeptr
        flag=True
    return flag


 #Q1 d ii
if addnode(linklist,emptylist,startpointer) == False:
     print("node not added successfully")
else:
     print("node added successfully")


outputnodes (linklist,startpointer)



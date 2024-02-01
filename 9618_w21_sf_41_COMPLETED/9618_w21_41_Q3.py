arraynodes=[[0 for i in range (3)   ]for j in range    (20)]
rootpointer=-1
freenode=0

def addnode(arraynodes,rootpointer,freenode):
    nodedata=input("input node data")
    if freenode <= 19:
        arraynodes[freenode][0]=-1
        arraynodes[freenode][1]=nodedata
        arraynodes[freenode][2]=-1

        if rootpointer== -1:
            rootpointer=0
        else:
            placed=False
            currentnode=rootpointer
            while placed==False:
                if nodedata < arraynodes[currentnode][1]:
                    if arraynodes[currentnode][0] == -1:
                        arraynodes[currentnode][0]=freenode
                        placed=True
                    else:
                        currentnode=arraynodes[currentnode][0]
                else:
                    if arraynodes[currentnode][2]==-1:
                        arraynodes[currentnode][2]=freenode
                        placed=True
                    else:
                        currentnode=arraynodes[currentnode][2]
        freenode+=1
    return arraynodes,rootpointer,freenode
def printall(arraynodes):
    for x in range (20):
        print(arraynodes[x][0],"",arraynodes[x][1],"",arraynodes[x][2])

for y in range(0,10):
    arraynodes, rootpointer, freenode = addnode(arraynodes,rootpointer,freenode)
printall(arraynodes)

def inorder(rootnode,arraynode):
    if arraynodes [rootnode][0]!=-1:
        inorder(arraynodes [rootnode][0],arraynodes)
    print(arraynodes[rootnode][1])
    if arraynodes[rootnode][2]!=-1:
        inorder(arraynodes[rootnode][2],arraynodes)
inorder(rootpointer,arraynodes)








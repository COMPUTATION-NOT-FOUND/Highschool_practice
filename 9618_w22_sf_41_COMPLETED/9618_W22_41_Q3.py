

Arraynode=[[-1 for i in  range (3)]for j in range(20)]

freenode=6
rootpointer=0

Arraynode[0]=[1,20,5]
Arraynode[1]=[2,15,-1]
Arraynode[2]=[-1,3,3]
Arraynode[3]=[-1,9,4]
Arraynode[4]=[-1,10,-1]
Arraynode[5]=[-1,58,-1]
Arraynode[6]=[-1,-1,-1]

print(Arraynode)


def searchValue(root,valuefind):
    if root == -1:
        return -1
    elif Arraynode[root][1]==valuefind:
        return root
        if Arraynode[root][1]==-1:
            return -1

    if Arraynode[root][1]>valuefind:
        return searchValue(Arraynode[root][0],valuefind)
    if Arraynode[root][1]<valuefind:
        return searchValue(Arraynode[root][2],valuefind)



def postorder(rootnode):
    if Arraynode[rootnode][0]!=-1:
        postorder(Arraynode[rootnode][0])
    print(Arraynode[rootnode][1])
    if Arraynode[rootnode][2]!=-1:
        postorder(Arraynode[rootnode][2])


returned=searchValue(0,15)

if returned !=-1:
    print("value found at ",returned)
else:
    print("not found")

postorder(rootpointer)








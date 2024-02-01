queue=["" for i in range(20)]
startpointer=0
endpointer=0


def enqueue(data):
    global queue, startpointer, endpointer
    if endpointer!=20:
        if endpointer==0:
            queue[endpointer]=data
            endpointer+=1
            return True
        else:
            queue[endpointer]=data
            endpointer += 1
            return True
    else:
        return False


def readfile():
    x=input("input a file to read")
    try:
        file=open(x,"rt")
    except IOError:
        return -1
    y=file.readline().strip()
    flag=True
    while y!="" and flag !=False:
        flag=enqueue(y)
        print(flag)
        y = file.readline().strip()


    if flag==False:
        file.close()
        return 2

    else:
        file.close()
        return 1





output=readfile()
if output==1:
    print("all values successfully added")

elif output==2:
    print("not all values added")

else:
    print("file not found")


print(queue)
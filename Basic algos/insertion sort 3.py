mylist = [70,46,43,27,57,41,45,21,14]
upperbound=9
lowerbound=0

for index in range(lowerbound,upperbound):
    key = mylist[index]
    place= index-1
    if mylist[place]> key:
        while place >= lowerbound and mylist[place] > key:
            temp = mylist[place+1]
            mylist[place+1]=mylist[place]
            mylist[place]=temp
            place=place -1
        mylist[place +1] = key
print(mylist)


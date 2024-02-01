
def unknown(x,y):
    if x < y :
        print(x+y)
        return(unknown(x+1,y)*2)
    else:
        if x==y:
            return 1
        else:
            print (x+y)
            return (unknown(x-1,y)//2)

print("10 and 15")
print(unknown(10, 15))
print("10 and 10")
print(str(unknown(10, 10)))
print("15 and 10")
print(str(unknown(15, 10)))


def iterativeunknown(x,y):
    total=1
    while x != y:
       if x < y:
           print(x+y)
           x+=1
           total=total*2
       else:
            print(x+y)
            x-=1
            total=total//2
    return(total)

print("10 and 15")
print(str(iterativeunknown(10, 15)))
print("10 and 10")
print(str(iterativeunknown(10, 10)))
print("15 and 10")
print(str(iterativeunknown(15, 10)))





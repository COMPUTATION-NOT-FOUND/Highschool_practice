stack=[ 0 for i in range (0,10)]
basepointer=0
toppointer=-1
stackfull=10
item=None

def pop():
    global toppointer,basepointer,item
    if toppointer==basepointer -1:
        print("stack is empty,cannot pop")
    else:
        item=stack[toppointer]
        stack[toppointer]=0
        toppointer= toppointer-1
def push(item):
    global toppointer
    if toppointer< stackfull-1:
        toppointer= toppointer+1
        stack[toppointer]=item
    else:
        print("stack is full value cannot be pushed")

for i in range(11):
    push(i)
print(stack)
for x in range(10):
    pop()
    print(item)
print(stack)

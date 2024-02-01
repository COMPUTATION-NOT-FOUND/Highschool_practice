dataarray = [2, 6, 7, 9, 10, 1, 3, 4, 5, 8]

def bubblesort():
    total = len(dataarray) - 1
    swap = True
    while swap and total >= 0:
        swap = False
        for k in range(total):
            if dataarray[k] > dataarray[k+1]:
                dataarray[k], dataarray[k+1] = dataarray[k+1], dataarray[k]
                swap = True
        total -= 1

bubblesort()
print(dataarray)
# Write your code here :-)

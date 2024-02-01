# Write your code here :-)
filedata = [["",""]for i in range (11)]

def readhighscores():
    filename="Highscore.txt"
    file=open(filename,"rt")
    for j in range (11):
        filedata[j][0]=file.readline()
        filedata[j][1]=file.readline()
    file.close
def outputhighscores():
    for k in range (11):
        print(filedata[k][0],"",filedata[k][1])

readhighscores()
outputhighscores()

username="ABCD"
while len(username)!= 3:
    username=(input("enter username :")).strip()
score=-1
while score <1 or score>100000:
    score=int((input("inputscore pls :")).strip())

def arrange(username,score):
    filedata[10][0]=username
    filedata[10][1]=score
    for ptr in range(1,11):
        temp1=int(filedata[ptr][1])
        temp2=filedata[ptr][0]
        comp_ptr=ptr-1
        while int(filedata[comp_ptr][1])<temp1 and comp_ptr>-1:
            filedata[comp_ptr+1][1]=filedata[comp_ptr][1]
            filedata[comp_ptr+1][0]=filedata[comp_ptr][0]
            comp_ptr-=1
        filedata[comp_ptr+1][0]=temp2
        filedata[comp_ptr+1][1]=temp1

arrange(username,score)
outputhighscores()

def writetopten():
    Filename = " NewHighScore.txt"
    Filename = open(Filename, 'wt')
    for x in range(0, 10):
        Filename.write(str(filedata[x][0]) + '\n')
        Filename.write(str(filedata[x][1]) + '\n')
        Filename.close
writetopten()




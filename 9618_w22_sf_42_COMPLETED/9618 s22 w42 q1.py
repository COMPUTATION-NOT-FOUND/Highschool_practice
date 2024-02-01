
#DECLARE Jobs: ARRAY[0:99,0:1]
global NumberofJobs
jobs=[[0]*2]*100
print(jobs)

def intialise():
    global NumberofJobs,jobs
    for x in range(100):
        for y in range(2):
          jobs[x][y]=-1
    NumberofJobs=0
def addJob(jobnumber,priority):
    global NumberofJobs,jobs
    if NumberofJobs<100:
        jobs[NumberofJobs]=[jobnumber,priority]

        NumberofJobs+=1

intialise()
print(jobs)
addJob(12,10)
addJob(526,9)
addJob(33,8)
addJob(12,9)
addJob(78,10)
print(jobs)

def insertionsort():
    global NumberofJobs,jobs
    for ptr in range(1,NumberofJobs+1):
        for comp_ptr in range (0,ptr):
            if jobs[ptr][1] > jobs[comp_ptr][1]:
                temp=jobs[ptr]
                for i in range (ptr,comp_ptr,-1):
                    jobs[i]=jobs[i-1]
                jobs[comp_ptr]=temp


insertionsort()
print(jobs)



#def printarray():
 #   global NumberofJobs
  #  for i in range(NumberofJobs):
   #     print(jobs[0][NumberofJobs]"priority"jobs[1][NumberofJobs])














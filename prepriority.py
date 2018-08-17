#!/usr/bin/env python
import sched
import time
import copy
import psutil

#scheduler = sched.scheduler(time.time, time.sleep)

#creating processes

process_queue = []
total_wtime = 0
total_ttime=0
total_time=0
co=0
k=0
sp=0
sp1=0
#tt=[]
#wt=[]
n = int(raw_input('Enter the total no of processes: '))
for i in xrange(n):
    process_queue.append([])#append a list object to the list
    process_queue[i].append(raw_input('Enter p_name: '))
    process_queue[i].append(int(raw_input('Enter p_arrival: ')))
    total_wtime += process_queue[i][1]
    process_queue[i].append(int(raw_input('Enter p_bust: ')))
    total_time=total_time+process_queue[i][2]
    filenames=((raw_input('Enter filenames to be accessed by the process: '))).split()
    process_queue[i].append(len(filenames))
    children=((raw_input('Enter names of the children the process has '))).split()
    process_queue[i].append(len(children))
    process_queue[i].append(int(raw_input('Enter default priority: ')))
    process_queue[i].append(int(i+1029))
    process_queue[i].append(0)
    process_queue[i].append(0)
    print ''

#process_queue.sort(key = lambda process_queue:process_queue[0])

print process_queue
#print process_queue[0][5],process_queue[1][5],process_queue[2][5]




def setpriority():
    #burstsort=copy.deepcopy(process_queue)
    process_queue.sort(key = lambda process_queue:process_queue[2])
    print process_queue
    
    for i in xrange(n):
        priority=process_queue[i][5]
        #increase priority as per no of open files.
        priority-=process_queue[i][3]
        #increase depending upon no of dependent processes
        priority-=process_queue[i][4]
        process_queue[i][5]=priority-(n-i)
   
setpriority()
print process_queue
process_queue.sort(key = lambda process_queue:process_queue[0])
scheduler = sched.scheduler(time.time, time.sleep)
#Running threads
def process_a(name):
    print 'EVENT A STARTED AT :', time.time(), 'I am process', name
    print psutil.cpu_percent(interval=None)
    print psutil.cpu_stats()
    f1 = open('yfile.txt', 'w')
    #f1.close()
    f2 = open('pyfile.txt','r')
    contents=f2.read()
    print(contents)
    p = psutil.Process()
    print p.open_files()
    f1.close()
    f2.close()
    print 'EVENT A FINISHED AT :', time.time(), 'I am process', name
def process_b(name):
    print 'EVENT B STARTED AT :', time.time(), 'I am process', name
    print 'EVENT B FINISHED AT :', time.time(), 'I am process', name
    print psutil.cpu_percent(interval=None)
    print psutil.cpu_stats()

def process_c(name):
    print 'EVENT C STARTED AT :', time.time(), 'I am process', name
    print 'EVENT C FINISHED AT :', time.time(), 'I am process', name
    print psutil.cpu_percent(interval=None)
    print psutil.cpu_stats()

def process_d(name):
    print 'EVENT D STARTED AT :', time.time(), 'I am process', name
    print 'EVENT D FINISHED AT :', time.time(), 'I am process', name

now = time.time()
print 'start....',now

def premptive():
    co=0
    sp=0
    sp1=0
    k=0
    for i in xrange(total_time):
        small=999
        for j in xrange(co,n):
            if k >= process_queue[j][1]:
                co+=1
        for j in xrange(co):
            if small > process_queue[j][5] and process_queue[j][2] != 0:
                small=process_queue[j][5]
                sp=process_queue[j][5]
                sp1=j

            if sp1==0:
                scheduler.enterabs(now+2,1, process_a, ('A',))
                #scheduler.run()
            elif sp1==1:
                scheduler.enterabs(now+2,1, process_b, ('B',))
                #scheduler.run()
            elif sp1==2:
                scheduler.enterabs(now+2,1, process_c, ('C',))
                #scheduler.run()
            elif sp1==3:
                scheduler.enterabs(now+2,1, process_d, ('D',))
                #scheduler.run()
            scheduler.run()

        process_queue[sp1][2]=process_queue[sp1][2]-1

        if process_queue[sp1][2]==0:
            process_queue[sp1][8]=i

        for j in xrange(n):
            if process_queue[j][2] != 0 and j != sp1:
                process_queue[j][7]+=1

        k+=1


    print 'end for total'
    

'''scheduler.enterabs(now+2, process_queue[0][5], process_a, ('A',))
scheduler.enterabs(now+2, process_queue[1][5], process_b, ('B',))
scheduler.enterabs(now+2, process_queue[2][5], process_c, ('C',))
scheduler.run()'''

process_queue.sort(key = lambda process_queue:process_queue[1])
print process_queue

premptive()

process_queue.sort(key = lambda process_queue:process_queue[0])

for j in xrange(n):
    total_wtime+=process_queue[j][7]
    total_ttime+=process_queue[j][8]

AvgWait=total_wtime/n
AvgTurn=total_ttime/n

print process_queue
print 'AVERAGE WAITING TIME IS' ,AvgWait
print 'AVERAGE TURNAROUND TIME IS' ,AvgTurn







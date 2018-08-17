#!/usr/bin/env python
import sched
import time
import copy
import psutil

#scheduler = sched.scheduler(time.time, time.sleep)

#creating processes

process_queue = []
total_wtime = 0
n = int(raw_input('Enter the total no of processes: '))
for i in xrange(n):
    process_queue.append([])#append a list object to the list
    process_queue[i].append(raw_input('Enter p_name: '))
    process_queue[i].append(int(raw_input('Enter p_arrival: ')))
    total_wtime += process_queue[i][1]
    process_queue[i].append(int(raw_input('Enter p_bust: ')))
    filenames=((raw_input('Enter filenames to be accessed by the process: '))).split()
    process_queue[i].append(len(filenames))
    children=((raw_input('Enter no_of_ children the process has '))).split()
    process_queue[i].append(len(children))
    process_queue[i].append(int(raw_input('Enter default priority: ')))
    process_queue[i].append(int(i+1029))
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
    '''print psutil.cpu_percent(interval=None)
    print psutil.cpu_stats()
    f1 = open('yfile.txt', 'w')
    #f1.close()
    f2 = open('pyfile.txt','r')
    contents=f2.read()
    print(contents)
    p = psutil.Process()
    print p.open_files()
    f1.close()
    f2.close()'''
    print 'EVENT A FINISHED AT :', time.time(), 'I am process', name
def process_b(name):
    print 'EVENT B STARTED AT :', time.time(), 'I am process', name
    print 'EVENT B FINISHED AT :', time.time(), 'I am process', name
    '''print psutil.cpu_percent(interval=None)
    print psutil.cpu_stats()'''

def process_c(name):
    print 'EVENT C STARTED AT :', time.time(), 'I am process', name
    print 'EVENT C FINISHED AT :', time.time(), 'I am process', name
    '''print psutil.cpu_percent(interval=None)
    print psutil.cpu_stats()'''

now = time.time()
print 'start....',now

scheduler.enterabs(now+2, process_queue[0][5], process_a, ('A',))
scheduler.enterabs(now+2, process_queue[1][5], process_b, ('B',))
scheduler.enterabs(now+2, process_queue[2][5], process_c, ('C',))
scheduler.run()





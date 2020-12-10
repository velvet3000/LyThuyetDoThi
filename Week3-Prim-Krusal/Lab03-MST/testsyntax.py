from queue import PriorityQueue
queue = {(1,2): 5}
queue[(2,3)] =  7
temp = queue.keys()
for key in queue.keys() :
    print (key[0])
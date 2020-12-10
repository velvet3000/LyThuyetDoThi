import numpy as np
import queue as PriorityQueue
def main():
    matrix = readFile("MST.txt").astype(int)
    prim(matrix)
    weightNode = getWeight(matrix)
def readFile(path):
    data = np.loadtxt(path)
    return data
def getNearly(matrix,vertices):
    result = []
    for i in range(len(matrix[vertices])):
        if matrix[vertices][i]>0:
            result.append(i)
    return result
def getWeight(matrix):
    weightNode = {}
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] > 0:
                weightNode[i,j] = matrix[i][j]
    return weightNode
def isCircle(u, element):
    if element[1] not in u:
        return True
    return False
def findKeyMin(u, queue):
    newqueue = queue.copy()
    for i in list(newqueue):
        if i[1] in u and i[0] in u:
            del newqueue[i]
    return min(newqueue, key=newqueue.get)
def prim(matrix):
    v_u = [] #create list of vertice
    for i in range(len(matrix)):
        v_u.append(i)
    u = []
    weightNode = getWeight(matrix)
    # queue = PriorityQueue()
    # isCircle = {}
    # n_v=matrix.shape[0]
    # np.random.seed(0)
    # start_v=np.random.randint(0,n_v-1)
    queue = {}
    start_v = v_u.pop(0)
    edges=[]
    while True:
        u.append(start_v)
        print("u", u)
        print("edge:", edges)
        if len(u) == len(matrix):
            break
        nearly = getNearly(matrix,start_v)

        print("start_v: {}, {}".format(start_v,nearly))
        for element in nearly:
            queue[start_v,element] = weightNode[start_v,element]
    # find key_min
        print("queue: ", queue)

        key_min = findKeyMin(u,queue)
        print("key_min", key_min)
        print("value k: ",key_min[1])
        v_u.remove(key_min[1])
        edges.append(key_min)
        start_v = key_min[1]
        del queue[key_min]
        print("u", u)
        print("v_u current:", v_u)
        print("\n")



    

main()
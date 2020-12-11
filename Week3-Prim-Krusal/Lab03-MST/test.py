import numpy as np
import queue as PriorityQueue
import operator
from collections import OrderedDict
def main():
    matrix = readFile("MST.txt").astype(int)
    kruskal(matrix)
    # prim(matrix)
    # weightNode = getWeight(matrix)
    # print(weightNode)
def createTag(allEdges):
    tag = {}
    for i in allEdges:
        tag[i[0]] = [i[0], i[0]]
        tag[i[1]] = [i[1],i[1]]
    return tag
def notCycle(item, tag):
    # if item[0] == tag[item[1]][0] or item[0] == tag[item[1]][1] and item[1] == tag[item[0]][1] or item[1] == tag[item[0]][1]:
    # if tag[item[0]][0] == tag[item[1]][0] or tag[item[0]][0] == tag[item[1]][0] and tag[item[0]][0]
    # if tag[item[0]][0] in tag[item[1]] and tag[item[0]][1] in tag[item[1]]
    print("check{}, min:{}, max{}".format(item[0],tag[item[0]][0],tag[item[0]][1]))
    print("check{}, min:{}, max{}".format(item[1],tag[item[1]][0],tag[item[1]][1]))
    if tag[item[0]][0] in tag[item[1]] and tag[item[0]][1] in tag[item[1]]:
        print("false")
        return False #Kiểm tra tag min max của đỉnh có trùng với nhau ko
    print("true")
    return True
def setTag(tag, edge):
    # min = tag[edges[0][0]][0]
    # orMin = min
    # max = tag[edges[0][1]][1]
    # print ("test min: ",min)
    # print("testmax : ",max)
    # for i in edges:
    #     if i[0] < min:
    #         min = i[0]
    #     if i[1] > max:
    #         max = i[1]
    # for edge in edges:
    #     if tag[edge[0]][0] == orMin:
    #         tag[edge[0]] = [min,max]
    #         tag[edge[1]] = [min,max]
    print(edge)
    min = tag[edge[0]][0] #Tìm giá trị min, max trong 2 đỉnh để gán
    max = tag[edge[0]][1]
    if tag[edge[1]][0] < min:
        min = tag[edge[1]][0]
    if tag[edge[1]][1] > max:
        max =tag[edge[1]][1]
    tag[edge[1]] = [min,max]
    tag[edge[0]] = [min,max]
    print("{}: {}".format(edge[1],tag[edge[1]]))
    print("{}: {}".format(edge[0],tag[edge[0]]))
    for element in tag.keys(): #gán min max cho các đỉnh có liên kết với đỉnh đag xét
        if tag[element][0] == min:
            tag[element] = [min,max]
        if tag[element][1] == max:
            tag[element] = [min,max]
    return


def kruskal(matrix):
    print(getWeight(matrix))
    allEdges = list(getWeight(matrix)) #get all edges with their weight
    tag = createTag(allEdges) #tag with [min,max] of item
    print(tag.items())
    edges = [allEdges.pop(0)]              #return value
    while len(edges) < len(matrix):
        checkItem = allEdges.pop(0)
        print((checkItem[0],checkItem[1]))
        print("edges now: ",edges)
        # if notExist(checkItem[0],edges) or notExist(checkItem[1],edges):
        if notCycle(checkItem, tag):
            edges.append(checkItem)
            setTag(tag,checkItem)
        print("\n")
# def getTag():

    
def notExist(vertice, allEdges):
    for e in allEdges:
        if vertice == e[0] or vertice == e[1]:
            return False
    return True
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
    sorted_dict = {}
    # for i in reversed(range(len(matrix))):
    #     for j in range(len(matrix)):
    #         if matrix[i][j] > 0 and (i,j) not in list(weightNode.keys()) and (j,i) not in list(weightNode.keys()):
    #             weightNode[j,i] = matrix[i][j]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[j][i] > 0 and (i,j) not in list(weightNode.keys()) and (j,i) not in list(weightNode.keys()):
                weightNode[i,j] = matrix[j][i]
    sorted_tuples = sorted(weightNode.items(), key=operator.itemgetter(1))
    for k, v in sorted_tuples:
        sorted_dict[k] = v
    # for i in range(len(weightNode)):
    #     for j in range(len(weightNode)):
    #         if weightNode[i][j]
    # a = list(weightNode.items())

    return sorted_dict
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
            if element not in u:
                if (start_v, element) in weightNode:
                    queue[start_v,element] = weightNode[start_v,element]
                else:
                    queue[start_v,element] = weightNode[element,start_v]
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
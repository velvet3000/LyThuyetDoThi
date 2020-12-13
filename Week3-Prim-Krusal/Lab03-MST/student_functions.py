import numpy as np
import operator

def DFS(matrix, start, end):
    """
    BFS algorithm:
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        start node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes, each key is a visited node,
        each value is the adjacent node visited before it.
    path: list
        Founded path
    """
    # TODO: 
   
   
    path=[]
    visited={}
    
    return visited, path

def BFS(matrix, start, end):
    """
    DFS algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        start node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited 
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """

    # TODO: 
    
    path=[]
    visited={}
   
    return visited, path

def UCS(matrix, start, end, pos):
    """
    Uniform Cost Search algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        start node
    end: integer
        ending node
    pos: dictionary. keys are nodes, values are positions
        positions of graph nodes
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path=[]
    visited={}
    return visited, path


def Prim(matrix):
    """
    BFS algorithm:
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        start node
    end: integer
        ending node
    
    Returns
    ---------------------
    edges: list
        List of founded edges in spanning tree (sort by search order)
        example: [[1,2],[3,4],[4,5]]
    """
    # TODO: 
    weightNode = getWeight(matrix)
    n_v=matrix.shape[0]
    np.random.seed(0)
    start_v=np.random.randint(0,n_v-1)
    queue = {}
    v_u = [] #create list of vertice
    for i in range(len(matrix)):
        if i != start_v:
            v_u.append(i)
    u = []
    edges=[]
    while True:
        u.append(start_v)
        if len(u) == len(matrix):
            break
        nearly = getNearly(matrix,start_v)
        for element in nearly: #Thêm các cạnh kề vào queue
            if element not in u:
                if (start_v, element) in weightNode:
                    queue[start_v,element] = weightNode[start_v,element]
                else:
                    queue[start_v,element] = weightNode[element,start_v]
        key_min = findKeyMin(u,queue) #find key min
        v_u.remove(key_min[1])
        edges.append(key_min)
        start_v = key_min[1]
        del queue[key_min]
    return edges

def Kruskal(matrix):
    """
    DFS algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        start node
    end: integer
        ending node
    
    Returns
    ---------------------
   edges: list
        List of founded edges in spanning tree (sort by search order)
        example: [(1,2),(3,4),(4,5)]
    """ 
    # TODO: 

    allEdges = list(getWeight(matrix).keys()) #get all edges with their weight
    tag = createTag(allEdges) #tag with [min,max] of item
    edges = []              #return value
    while len(edges) != len(matrix)-1:
        checkItem = allEdges.pop(0)
        if notCycle(checkItem, tag):  #check if add edge becoming a cycle of not
            edges.append(checkItem)
            setTag(tag,checkItem)
    return edges

def getWeight(matrix):
    weightNode = {}
    sorted_dict = {}
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[j][i] > 0 and (i,j) not in list(weightNode.keys()) and (j,i) not in list(weightNode.keys()):
                weightNode[i,j] = matrix[j][i]
    sorted_tuples = sorted(weightNode.items(), key=operator.itemgetter(1))
    for k, v in sorted_tuples:
        sorted_dict[k] = v
    return sorted_dict

def findKeyMin(u, queue):
    newqueue = queue.copy()
    for i in list(newqueue):
        if i[1] in u and i[0] in u:
            del newqueue[i]
    return min(newqueue, key=newqueue.get)
    
def getNearly(matrix,vertices):
    result = []
    for i in range(len(matrix[vertices])):
        if matrix[vertices][i]>0:
            result.append(i)
    return result

def createTag(allEdges):
    tag = {}
    for i in allEdges:
        tag[i[0]] = [i[0], i[0]]
        tag[i[1]] = [i[1],i[1]]
    return tag

def setTag(tag, edge):
    min = tag[edge[0]][0] #Tìm giá trị min, max trong 2 đỉnh để gán
    max = tag[edge[0]][1]
    if tag[edge[1]][0] < min:
        min = tag[edge[1]][0]
    if tag[edge[1]][1] > max:
        max =tag[edge[1]][1]
    tag[edge[1]] = [min,max]
    tag[edge[0]] = [min,max]
    for element in tag.keys(): #gán min max cho các đỉnh có liên kết với đỉnh đag xét
        if tag[element][0] == min:
            tag[element] = [min,max]
        if tag[element][1] == max:
            tag[element] = [min,max]
    return

def notCycle(item, tag):
    if tag[item[0]][0] in tag[item[1]] and tag[item[0]][1] in tag[item[1]]:
        return False #Kiểm tra tag min max của đỉnh có trùng với nhau ko
    return True
import numpy as np

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

def getNearly(matrix,vertices):
    result = []
    for i in range(len(matrix[vertices])):
        if matrix[vertices][i]>0:
            result.append(i)
    return result
def getWeight(matrix):
    weightNode = {}
    for i in reversed(range(len(matrix))):
        for j in range(len(matrix)):
            if matrix[i][j] > 0 and (i,j) not in list(weightNode.keys()) and (j,i) not in list(weightNode.keys()):
                weightNode[i,j] = matrix[i][j]
    return weightNode

def findKeyMin(u, queue):
    newqueue = queue.copy()
    for i in list(newqueue):
        if i[1] in u and i[0] in u:
            del newqueue[i]
    return min(newqueue, key=newqueue.get)
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
    v_u = [] #create list of vertice
    for i in range(len(matrix)):
        v_u.append(i)
    u = []
    weightNode = getWeight(matrix)
    queue = {}
    start_v = v_u.pop(0)
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
    edges=[]
    return edges

    

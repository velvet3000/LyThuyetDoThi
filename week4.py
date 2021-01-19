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
    path = []
    visited = {}
    return visited,path

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
    edges=[]
    n_v=matrix.shape[0]
    np.random.seed(0)
    start_v=np.random.randint(0,n_v-1)
    
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

def ConnectedComponents(matrix):
    """
     Connected Components
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    
    Returns
    ---------------------
   edges: list
        example: [
            [4,6],[5,6],[6,7]], // component 1
            [[1,3],[1,2],[2,0]],  // component 2
            [[9,10],[9,11],[8,10]  // component 3
        ]
    """ 

    # TODO: 
    vertices = {}
    edges = []
    component = []
    for i in range(len(matrix)):
        vertices[i] = 0
    vertices[list(vertices.keys())[0]] = 1
    for v in vertices:
        nearly = getNearly(matrix,v)
        if vertices[v] == 0 and notConnect(component,nearly) or v == list(vertices.keys())[-1]:
            edges.append(component)
            component = []
        for n in nearly:
            if vertices[n] == 0:
                component.append([v,n])
                vertices[n] = 1
    print(edges)
    return(edges)

def notConnect(component, nearly):
    for i in component:
        if i[0] in nearly or i[1] in nearly:
            return False
    return True
def getNearly(matrix,vertices):
    result = []
    for i in range(len(matrix[vertices])):
        if matrix[vertices][i]>0:
            result.append(i)
    return result

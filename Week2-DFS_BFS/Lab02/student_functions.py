import numpy as np

def getNearly(matrix,vertices):
    result = []
    for i in range(len(matrix[vertices])):
        if matrix[vertices][i]>0:
            result.append(i)
    return result  
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
    path = [end]
    stack =[start]
    visited = {start:-1}
    while True:
        start = stack.pop()
        nearly = getNearly(matrix,start)
        for element in nearly:
            if element not in visited:
                stack.append(element)
                visited[element] = start
        if start == end:
            nodeConnected = visited[end]
            for i in reversed(list(visited.keys())):
                if i == nodeConnected:
                   path.insert(0,i)
                   nodeConnected = visited[i]
                if visited[i] == -1:
                    break
            break
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
    
    path = [end]
    queue =[start]
    visited = {start:-1}
    while True:
        start = queue.pop(0)
        nearly = getNearly(matrix,start)
        for element in nearly:
            if element not in visited:
                queue.append(element)
                visited[element] = start
        if start == end:
            nodeConnected = visited[end]
            for i in reversed(list(visited.keys())):
                if i == nodeConnected:
                   path.insert(0,i)
                   nodeConnected = visited[i]
                if visited[i] == -1:
                    break
            break
    return visited,path


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
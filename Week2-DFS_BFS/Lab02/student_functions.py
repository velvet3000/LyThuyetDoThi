import numpy as np
# Đã fix lại lỗi visited ở bài trước

def getNearly(matrix,vertices):
    result = []
    for i in range(len(matrix[vertices])):
        if matrix[vertices][i]>0:
            result.append(i)
    return result  
def getParent(vertice,matrix,visited):
    parent = []
    for i in range(len(matrix)):
        if matrix[i][vertice] > 0:
            parent.append(i)
    for element in visited:
        if element in parent:
            return element
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
    visited = {}
    while len(stack) != 0:
        if start == end:
            nodeConnected = visited[end]
            for i in reversed(list(visited.keys())):
                if i == nodeConnected:
                   path.insert(0,i)
                   nodeConnected = visited[i]
            break # Tới end nên dừng lại
        if len(visited) == 0:
            visited[stack[len(stack)-1]] = -1
        else:
            visited[stack[len(stack)-1]] = start  
        start = stack.pop()
        nearly = getNearly(matrix,start)
        for element in nearly:
            if element not in visited and element not in stack:
                stack.append(element)
    print(visited,path)
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
    
    path = [end]
    queue =[start]
    visited = {}
    while len(queue) != 0:
        if start == end:
            nodeConnected = visited[end]
            for i in reversed(list(visited.keys())):
                if i == nodeConnected:
                   path.insert(0,i)
                   nodeConnected = visited[i]
            break # Tới end nên dừng lại
        if len(visited) == 0:
            visited[queue[0]] = -1
        else:
            visited[queue[0]] = getParent(queue[0], matrix,visited)
        start = queue.pop(0)
        nearly = getNearly(matrix,start)
        for element in nearly:
            if element not in visited and element not in queue:
                queue.append(element)
    print(visited,path)
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
    print (pos)
    return visited, path
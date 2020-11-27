import numpy as np

def getNearly(matrix,vertices):
    result = []
    for i in range(len(matrix[vertices])):
        if matrix[vertices][i]>0:
            result.append(i)
    return result  
def checkNearlyInHistory(nearly,history):
    for i in nearly:
        if i not in history:
            return True
    return False         
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
    path = [start]
    visited = {start:-1}
    history = [start]  #Biến history dùng để so sánh node với các đường đã đi
    while True:
        nearly = getNearly(matrix,start)
        check = False # kiểm tra trường hợp node hết đường đi
        for i in range(len(nearly)):
            nearlyChild = getNearly(matrix,nearly[i])
            if nearly[i] not in path:
                if checkNearlyInHistory(nearlyChild,history) == True or nearly[i] not in history:
                    path.append(nearly[i])
                    history.append(nearly[i])
                    visited[nearly[i]] = start
                    start = nearly[i]
                    check = False
                    break
            else:
                check = True
        if(check == True):
            # Nếu node hết đường sẽ quay lai node truoc do
            visited.pop(path[len(path)-1])
            path.pop()
            start = path[len(path)-1]
            history.append(start)
        if start == end:
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
    
    result = [start]
    visited = {start:-1}
    history = [start]
    while True:
        nearly = getNearly(matrix, start)
        newstart=-1
        for element in nearly:
            if element not in visited and element != start:
                result.append(element)
                visited[element] = start
                newstart = element
        start = newstart
        # New step
        if start == end:
            nodeConnected = visited[end]
            path = [end]
            for i in reversed(list(visited.keys())):
                if i == nodeConnected:
                   path.insert(0,i)
                   nodeConnected = visited[i]
                   print(result)
                if visited[i] == -1:
                    break
            for i in list(visited.keys()):
                if i not in path:
                    del visited[i]
            break
        history.append(start)
        start = result[1]
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
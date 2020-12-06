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
def getWeight(matrix):
    weightNode = {}
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] > 0:
                weightNode[i,j] = matrix[i][j]
    return weightNode
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
        start = queue.pop(0)
        if len(visited) == 0:
            visited[start] = -1
        else:
            visited[start] = getParent(start, matrix,visited)
        nearly = getNearly(matrix,start)
        for element in nearly:
            if element not in visited and element not in queue:
                queue.append(element)
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
    path = [end]
    queue = {start:0}
    visited = {}
    weightNode = getWeight(matrix)
    while True:
        if start == end:
            nodeConnected = visited[end]
            for i in reversed(list(visited.keys())):
                if i == nodeConnected:
                   path.insert(0,i)
                   nodeConnected = visited[i]
                if visited[i] == -1:
                    break
            break
        key_min = min(queue.keys(), key=(lambda k: queue[k]))
        start = key_min
        nearly = getNearly(matrix,start)
        if len(visited) == 0:
            visited[start] = -1
        else:
            visited[start] = getParent(start, matrix,visited)
        for element in nearly:
            if element not in visited and element not in queue:
                queue[element] = weightNode[start, element] + queue[start]
        queue.pop(key_min)
    return visited, path

def BestFS(matrix,start,end):
    path = [end]
    queue = {start:0}
    visited = {}
    weightNode = getWeight(matrix)
    while True:
        if start == end:
            nodeConnected = visited[end]
            for i in reversed(list(visited.keys())):
                if i == nodeConnected:
                   path.insert(0,i)
                   nodeConnected = visited[i]
                if visited[i] == -1:
                    break
            break
        key_min = min(queue.keys(), key=(lambda k: queue[k]))
        start = key_min
        queue.pop(key_min)
        nearly = getNearly(matrix,start)
        if len(visited) == 0:
            visited[start] = -1
        else:
            visited[start] = getParent(start, matrix,visited)
        for element in nearly:
            if element not in visited:
                queue[element] = weightNode[start, element]
        return visited,path

def astart(matrix,start,end,pos,weightNode):
    path = [end]
    queue = {start:0}
    visited = {start:-1}
    weightNode = getWeight(matrix)
    while True:
        key_min = min(queue.keys(), key=(lambda k: queue[k]))
        start = key_min
        if start == end:
            nodeConnected = visited[end]
            for i in reversed(list(visited.keys())):
                if i == nodeConnected:
                   path.insert(0,i)
                   nodeConnected = visited[i]
                if visited[i] == -1:
                    break
            break
        nearly = getNearly(matrix,start)
        for element in nearly:
            if element not in visited:
                queue[element] = weightNode[start, element] + queue[start] + getDistance(pos, element, end)
                visited[element] = start
        queue.pop(key_min)
    return visited,path

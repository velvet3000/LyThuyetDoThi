  # path=[1,0,6]
    # visited={1:-1, 1:0, 6:0, 3: 4}
import numpy as np
import math
def readFile(path):
    data = np.loadtxt(path)
    return data
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

def dfs(matrix,start,end):
    path = []
    visited = {}
    history = []
    path.append(start)
    history.append(start)
    visited[start] = -1
    
    temp = 0
    while True:
        nearly = getNearly(matrix,start)
        print("dinh: ", start)
        print("child: ", nearly)
        print("path: ",path )

        print("history: ", history)
        print("visited: ",visited)
        check = False # kiểm tra trường hợp node hết đường đi
        for i in range(len(nearly)):
            nearlyChild = getNearly(matrix,nearly[i])
            print("nearly child {} : {}".format(nearly[i],nearlyChild))
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
            # Quay lai node truoc do
            # visited.pop(path[len(path)-1])
            # visited[path[len(path)-1]] = start
            # visited[]
            path.pop()
            start = path[len(path)-1]
            history.append(start)
        if start == end:
            break
        print("new path;",path)
        print("new historyL ",history)
        print("new visited:", visited)
        temp += 1
        print("\n")

    print("final history: {} \n".format(history))
    print("final path: ", path)
    print("final visited:" , visited)

# def bfs(matrix,start,end):
#     path = []
#     visited = {}
#     history = []
#     path.append(start)
#     history.append(start)
#     visited[start] = -1 

#     while True:
#         print("start:",start)
#         print("path:", path)
#         nearly = getNearly(matrix, start)
#         check = False #Kiểm tra các phần tử trong đỉnh kề có phần từ nào = end
#         for element in nearly:
#             if(element == end):
#                 path.append(element)
#                 start = element
#                 check = True
#                 break
#         if(check == False):
#             for element in nearly:
#                 if element not in path and element not in history:
#                     path.append(element)
#         print("nearly {}: {}".format(start,nearly))
#         print("history:", history)
#         # path.pop(0)

#         print ("new path:", path)
#         print("new start:",start)
#         # New step
#         if start == end:
#             break
#         history.append(start)
#         start = path[1]
#         if element not in getNearly(matrix,path[1]):
#             start = path.pop(1)
            
#         print("\n")
def bfs(matrix,start,end):
    result = [start]
    visited = {start:-1}
    history = [start]
    while True:
        print("start:",start)
        print("path:", result)
        nearly = getNearly(matrix, start)
        newstart=-1
        for element in nearly:
            if element not in visited and element != start:
                result.append(element)
                visited[element] = start
                newstart = element
        start = newstart
        print("nearly {}: {}".format(start,nearly))
        print("history:", history)
        # path.pop(0)
        print("new visited: ", visited)
        print ("new path:", result)
        print("new start:",start)
        # New step
        if start == end:
            nodeConnected = visited[end]
            path = [end]
            print('result: ')
            for i in reversed(list(visited.keys())):
                if i == nodeConnected:
                   path.insert(0,i)
                   nodeConnected = visited[i]
                   print(result)
                if visited[i] == -1:
                    break
            # for i in list(visited.keys()):
            #     if i not in path:
            #         del visited[i]
            print("final path: ", path)
            print("final visited: ", visited)
            break
        history.append(start)
        start = result[1]
        
        print("\n")
def bfs2(matrix,start,end):
    path = [end]
    queue =[start]
    visited = {start:-1}
    # history = [start]
    while True:
        print("Queue: ",queue)
        start = queue.pop(0)
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
        print("start: {} \n nearly[: {}".format(start,nearly))
        for element in nearly:
            if element not in visited:
                queue.append(element)
                visited[element] = start
        print("visited: ", visited)
        print("\n")
    print("final path:" , path)
    print("final visited: ",visited)
def getWeight(matrix):
    weightNode = {}
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] > 0:
                weightNode[i,j] = matrix[i][j]
    return weightNode
def dfs2(matrix,start,end):
    path = [end]
    stack =[start]
    visited = {start:-1}
    while True:
        print ("stack:", stack)
        start = stack.pop()
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
        print("start: {} \n nearly[: {}".format(start,nearly))
        for element in nearly:
            if element not in visited:
                stack.append(element)
                visited[element] = start
        print("visted: {} ",format(visited))
        print("\n")
    print ("final path: ", path)
    print("final visted: ", visited)
def ucs(matrix,start,end,weightNode):
    path = [end]
    queue = {start:0}
    # queue = [start]
    visited = {start:-1}
    print(weightNode)
    while True:
        print("Queue: ",queue)
        key_min = min(queue.keys(), key=(lambda k: queue[k]))
        print (key_min)
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
        print("start: {} \n nearly[: {}".format(start,nearly))
        for element in nearly:
            if element not in visited:
                queue[element] = weightNode[start, element] + queue[start]
                visited[element] = start
        queue.pop(key_min)
        print("new queue:" , queue)
        print("visited: ", visited)
        print("\n")
    print("final path:" , path)
    print("final visited: ",visited)

def sortQueue(queue):
    for i in range(len(queue)-1):   
        print(i)
def bestfs(matrix,start,end,weightNode):
    path = [end]
    queue = {start:0}
    # queue = [start]
    visited = {start:-1}
    print(weightNode)
    while True:
        print("Queue: ",queue)
        if(len(queue)) != 0:
            key_min = min(queue.keys(), key=(lambda k: queue[k]))
            print (key_min)
            start = key_min
            queue.pop(key_min)
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
        print("start: {} \n nearly[: {}".format(start,nearly))
        for element in nearly:
            if element not in visited:
                queue[element] = weightNode[start, element]
                visited[element] = start
        print("new queue:" , queue)
        print("visited: ", visited)
        print("\n")
    print("final path:" , path)
    print("final visited: ",visited)
def getDistance(pos, begin, end):


    distance = math.sqrt((pos[begin][0] - pos[end][0])*(pos[begin][0] - pos[end][0])
                         + (pos[begin][1] - pos[end][1])*(pos[begin][1] - pos[end][1]))
    return distance
def astart(matrix,start,end,pos,weightNode):
    path = [end]
    queue = {start:0}
    # queue = [start]
    visited = {start:-1}
    print(weightNode)
    while True:
        print("Queue: ",queue)
        key_min = min(queue.keys(), key=(lambda k: queue[k]))
        print (key_min)
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
        print("start: {} \n nearly[: {}".format(start,nearly))
        for element in nearly:
            if element not in visited:
                queue[element] = weightNode[start, element] + queue[start] + getDistance(pos, element, end)
                visited[element] = start
        queue.pop(key_min)
        print("new queue:" , queue)
        print("visited: ", visited)
        print("\n")
    print("final path:" , path)
    print("final visited: ",visited)

def main():
    matrix = readFile("data.txt").astype(int)
    weightNode = getWeight(matrix)
    
    # bestfs(matrix,1,6,weightNode)
    print("\n\n")
    # print("pos: ",weightNode)
    pos = {0: [-0.08421155,  0.07048411], 1: [0.2486729 , 0.19773199], 2: [-0.37820785,  0.2237471 ], 3: [-0.17160918,  0.57472971], 4: [0.394171 , 0.3848759], 6: [-0.10487227, -1], 5: [0.09605695, -0.4515688]}
    print(pos)
    x = pos[0][0]
    y = pos[0][1]
    print(x)
    print(y)
    print("sum", y-x)
    distance = getDistance(pos,0, 1)
    print ("distance: ,",distance)
    # print (pos[0,1])
    # key_max = min(pos.keys(), key=(lambda k: pos[k]))
    # print (key_max)
    # ucs(matrix,start,end,pos)
    # bfs2(matrix,1,6)

main()
    # i = 0
    # while i < 12:
        # print ("dinh: ", start)
        # print("path",path)
        # print("visitted: ",visited)
        # nearly = getNearly(matrix, start)
        # print ("nearly:",nearly)
        # print("history: ", history)
        # check = False # kiểm tra trường hợp node hết đường đi
        # for element in nearly:
        #     if element not in path:
        #         start = element
        #         path.append(start)
          
        #         check = False
        #         break
        #     else:
        #         check = True
        # if check == True:
        #     path.pop()
        #     start = path[len(path)-1]
        #     check = False
        #     print("true")
        #     print("new pathh:",path)
        #     print("new start",start)
        # history.append(start)
        # if start == end:
        #     break
        # print("dinh moi: ", start)
        # print("\n")
        # i += 1
 
# def dfs(matrix,start,end):
#     path = []
#     visited ={}
#     path.append(start)
#     while start != end:
#         print ("dinh: ", start)
#         print("path",path)
#         print("visitted: ",visited)
#         nearly = getNearly(matrix, start)
#         print ("nearly:",nearly)
#         check = True #Kiem tra trường hợp hết đỉnh kề đã trong đường đã đi
#         for element in nearly:
#             if element not in path:
#                 visited[start] = element
#                 start = element
#                 path.append(element)
#                 check = False
#                 break
#         if check == False:
#             start 
#             check = True
#         print("\n")
# def ConditionNearlyAndHistory(matrix,vertices,history,path):
#     # nếu đỉnh kề của đỉnh trùng hết với các bước đã đi thì trả về giá trị False
#     nearly = getNearly(matrix,vertices)
#     print ("dinh xet: ",vertices)
#     print(nearly)
#     check = True
#     for i in nearly:
#         if i in path and i in history:
#             check = False
#             break
#     return check
# def dfs(matrix,start,end):
#     path = []
#     visited = {}
#     history = []
#     path.append(start)
#     history.append(start)
#     i = 0
#     while i < 12:
#         print ("dinh: ", start)
#         print("path",path)
#         print("visitted: ",visited)
#         nearly = getNearly(matrix, start)
#         print ("nearly:",nearly)
#         print("history: ", history)
#         check = False # kiểm tra trường hợp node hết đường đi
#         for element in nearly:
#             if element not in history:
#                 check = False
#                 path.append(element)
#                 history.append(element)
#                 visited[element] = start
#                 start = element
#                 break
#             else:
#                 check = True
#         if check == True:
#             print("true")          
#             print(path)
#             print(history)
#             print(start)
#             for element in reversed(history):
#                 if element not in nearly and element != start and ConditionNearlyAndHistory(matrix,element,history,path):
#                     print (element)
#                     start = element
#                     print (start)
#                     path.append(start)
#                     print("dinh moi: ", start)
#                     break
#             check = False
#         if start == end:
#             break   
        
#         print("\n")
#         i += 1
# def conditionNearlyInHistory(maxtrix,vertices,path,history):
#     nearly = getNearly(matrix,vertices)
#     print ("dinh xet: ",vertices)
#     print(nearly)
#     check = True
#     for i in nearly:
#         if i in path and i in history:
#             check = False
#             break
#     return check


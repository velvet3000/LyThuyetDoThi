  # path=[1,0,6]
    # visited={1:-1, 1:0, 6:0, 3: 4}
import numpy as np
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
            visited.pop(path[len(path)-1])
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

    print("final path: ", path)
    print("final history:", history)
    print("final visited:" , visited)

def main():
    matrix = readFile("data.txt")
    dfs(matrix, 0 ,6)

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


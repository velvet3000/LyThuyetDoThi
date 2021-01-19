V = 5
K = 1
path = []

def isSafe(v, graph, path, pos):
    if graph[pos-1][v] == 0:
        return False
    for i in range(pos):
        if path[i] == v:
             return False
    return True

def hamCycleUntil(graph, path, pos):
    if pos == V:
        if graph[path[pos-1]][path[0]] == 1:
            return True
        return False

    for v in range(V):
        if isSafe(v, graph, path, pos):
            path[pos] = v
            if hamCycleUntil(graph, path, pos+1) == True:
                return True
            path[pos] = -1
    return False

def hamCycle(graph):
    path = []
    for i in range(V):
        path.append(-1)
    path[0] = 0
    if hamCycleUntil(graph, path, 1) == False:
        print("0")
        return
    print("1")
    printSolution(path)


def printSolution(path):
    for i in range(V):
        print(path[i], end=", ")
    

# Eucler alogithm
#  
# def init(label, hc, count):
#     for i in range(V):
#         label.append(0)
#         hc.append(0)
#     label[K - 1] = 1
#     hc[0] = K - 1

# def Eucler(vertice, graph, hc, label):
#     if vertice == V-1:
#         printEuler(vertice)
#     else:
#         for i in range(V):
#             if graph[hc[vertice - 1]][i] > 0 and label[i] == 0:
#                 hc[vertice] = i
#                 label[i] = 1
#                 Eucler(vertice + 1, graph)
#                 label[i] = 0 
#                 hc[vertice] = 0 

# def printEucler(vertice):
#     for i in range(vertice):
#         print(hc[i])

def main():
    graph = [[0,1,0,1,0], [1,0,1,1,1], [0,1,0,0,1], [1,1,0,0,0], [0,1,1,0,0]]
    hamCycle(graph)

    # count = 0
    # label = []
    # hc = []
    # init(label,hc,count)
    # Eucler(5, graph, hc, label)

main()
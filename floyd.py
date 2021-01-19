INF = 9999
v = 4
def main():
    graph = [[0,   5,  INF, 10], [INF, 0,   3, INF], [INF, INF, 0,   1],[INF, INF, INF, 0]]
    floydWarshall(graph)

def printSolution(dist):
    print("Show the shortest distance distances between every pair of vertices")
    for i in range(v):
        for j in range(v):
            if dist[i][j] == INF:
                print("INF ",  end ="")
            else:
                print("{}   ".format(dist[i][j]), end =""),
        print("")
    
def floydWarshall(graph):
    dist = graph
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]; 
    printSolution(dist)

main()

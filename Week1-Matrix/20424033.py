import numpy as np
import operator
# My enviroment: I'm using Visual Studio Code
# To import numby, I'm running this line in Integrated Terminal: pip install numpy
#https://docs.google.com/spreadsheets/d/1YUoRfw-ES9mif7zuK5a8qPn0yY9ehRPzolk2e_fmHW8/edit#gid=0
def getWeight(matrix):
    weightNode = {}
    sorted_dict = {}
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[j][i] > 0 and (i,j) not in list(weightNode.keys()) and (j,i) not in list(weightNode.keys()):
                weightNode[i,j] = matrix[j][i]
    sorted_tuples = sorted(weightNode.items(), key=operator.itemgetter(1))
    for k, v in sorted_tuples:
        sorted_dict[k] = v
    return sorted_dict
def main():
   arr = readFile('data.txt')
   print(arr)
   print(getWeight(arr))
   print("Cau 1: ")
   if isUnDirectGraph(arr):
       print ("Là đồ thị vô hướng")
   else:
       print ("Là đồ thị có hướng")
   print("Câu 2:\n Danh sách đỉnh kề: ", *cau2(arr))
   print("Câu 3:\nDanh sách bậc của từng đỉnh theo thứ tự đỉnh: ", *cau3(arr))
   levelArray = cau3(arr)
   print("Câu 4:\nSố lượng đỉnh bậc chẵn: ", cau4(levelArray))
   print("Câu 5\nSố lượng đỉnh bậc lẻ: ", cau5(levelArray))
   print("Câu 6:\nSố lượng đỉnh treo: ", cau6(levelArray))
   print("Câu 7:\nSố lượng đỉnh cô lập: ", cau7(levelArray))

def readFile(path):
    data = np.loadtxt(path)
    return data

def isUnDirectGraph(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                return False
    return True

def cau2(arr):
    result = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] > 0:
                result.append(int(j + 1))
    return result

def cau3(arr):
    result = []
    if(isUnDirectGraph(arr)):
        for line in arr:
            result.append(sum(map(lambda i: i > 0, line)))
    else:
        total = 0
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i][j] > 0:
                    total += 1
                if arr[j][i] > 0:
                    total += 1
            result.append(total)
            total = 0
    return result


def cau4(arr):
    return sum(map(lambda i: i % 2 == 0, arr))

def cau5(arr):
    return sum(map(lambda i: i % 2 != 0, arr))

def cau6(arr):
    return sum(map(lambda i: i == 1, arr))

def cau7(arr):
    return sum(map(lambda i: i == 0, arr))

main()

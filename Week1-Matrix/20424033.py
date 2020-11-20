import numpy as np

# My enviroment: I'm using Visual Studio Code
# To import numby, I'm running this line in Integrated Terminal: pip install numpy

def main():
   arr = readFile('data.txt')
   print("Do thi: ")
   for line in arr:
       print (line)

   if cau1(arr):
       print ("Là độ thị vô hướng")
   else:
       print ("Là đồ thị có hướng")

   # cau2
   print("\nCâu 2:\n Danh sách đỉnh kề: ", *cau2(arr))
   # Cau3
   print("Danh sách bậc của từng đỉnh theo thứ tự đỉnh: ", cau7(arr))
   # Cau4  
   print("Số lượng đỉnh cô lập: ", cau7(arr))

def readFile(path):
    arr = []
    for line in open(path, 'r'):
        arr.append(list(map(int,line.rstrip("\n").split(" "))))
    return arr

def cau1(arr):
    print("\nCâu 1: ")
    i = 0
    for i in range(len(arr)):
        j = 0
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                return False
    return True

def cau2(arr):
    i = 0
    result = []
    for i in range(len(arr)):
        j = 0
        for j in range(len(arr)):
            if arr[i][j] > 0:
                result.append(int(j + 1))
    return result

def cau3(arr):
    result = []
    for line in arr:
        result.append(sum(map(lambda i: i > 0, line)))
    return result

def cau4(arr):
    count=0
    for line in arr:
        count += sum(map(lambda i: i % 2 == 0, line))
    return count

def cau5(arr):
    count=0
    for line in arr:
        count += sum(map(lambda i: i % 2 != 0, line))
    return count

def cau6(arr):
    count=0
    for line in arr:
        count += sum(map(lambda i: i == 1, line))
    return count

def cau7(arr):
    count=0
    for line in arr:
        count += sum(map(lambda i: i == 0, line))
    return count
    

main()
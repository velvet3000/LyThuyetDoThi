a = [1,2,3,4]
b = [5]
print (b)
b.append(6)
print(b)
c = {1: 2, 3: 4}
print (c[list(c)[0]])
for i in list(reversed(sorted(c.keys()))):
    print (i)
# print (c[1])
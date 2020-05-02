'''
a = [1, 1, 2, 3, 4]
b = []
b.append(a[0])
for i in range(len(a)):
    flag = 0
    for k in range(len(b)):
        if a[i] == b[k]:
            flag = 1
            break
    if flag == 0:
        b.append(a[i])
print(b)
'''
a = [1, 1, 2, 3, 4, 5]
b = [1, 2, 3]
c = []
c.append(a[0] and b[0])
for i in range(len(a)):
    flag = 0
    for k in range(len(b)):
        for j in range(len(c)):
            if b[k] == c[j]:
                flag = 1
                break
        if flag == 0:
            c.append(b[k])
    if a[i] == c[j]:
        flag = 1
        break
if flag == 0:
    c.append(a[i])
print(c)
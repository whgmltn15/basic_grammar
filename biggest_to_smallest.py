'''
a = [4, 5, 1, 3, 2]
for i in range(len(a)):
    for i in range(len(a)-1):
        if a[i] < a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
        print(a)
'''
a = [3, 5, 2, 7, 1]
for i in range(len(a)):
    for i in range(len(a)-1):
        if a[i] <= a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
        b = 0
        for i in range(len(a)):
            if a[b] > a[i]:
                b = i
print(a)

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = a[0]
for i in range(len(a)):
    if b < a[i]:
        b = a[i]
print(b)
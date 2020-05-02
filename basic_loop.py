'''
for i in range (10):
    print("*"*i)

for i in range (10):
    print("*"*(10-i))

for i in range (100):
    one = i % 10
    if(one%3 == 0 and one != 0):
        print("*")
    else:
        print(i)

for i in range (100):
    a = i % 10
    b = i // 10
    if b % 3 == 0 and a % 3 == 0:
        print("**")
    elif b % 3 == 0 or a % 3 == 0:
        print("*")
    else:
        print(i)

for i in range(1, 10):
    for j in range (1, 10):
        print("%d * %d = %d" % (i, j , j * i))

a = int(6)
b = int(3)
while True:
    c = int(input("Enter the number: "))
    if (c == 1):
        print(b + a)
    elif (c == 2):
        print(b - a)
    elif (c == 3):
        print (b * a)
    elif (c == 4):
        print (b // a)
    elif c == 10:
        break

i = 0
while True:
    i = (i + 1)
    print(i)
    if i == 100:
        break

i = 1
j = 1

while i != 10:

    i = i + 1
    j = 1

    while j != 10:
        j = j + 1
        print ("%d * %d = %d" % (i, j , j * i))

i = 1
j = 1

while True:
    i = i + 1
    j = 1

    if i == 10:
        break

    while True:
        j = j + 1
        print("%d * %d = %d" % (i, j, j * i))
        if j == 10:
            break

a = []
for i in range (1, 101):
    a.append(i)
for i in range (100):
    print(a[i])

a = [5, 3, 4, 2, 10]
b = 0
c = 3
b,c = c,b

for i in range (5):
    if a[i] < b:
        b = a[i]
        print (b)

a = int(input())
b = [2, 3, 5, 7]
c = 0
for i in range (2, a):
    if a % i == 0:
        c = 1
        break

if c == 0:
    print("소수아님")
elif c != 0:
    print("소수")

a = "xyz"
b = input()
c = 0
if len(b) == len(a):
    for i in range(len(a)):
        if a[i] != b[i]:
            c = 1
            break
    if c == 0:
        print("같다")
    else:
        print("다르다")
else:
    print("다르다")


def test_function(a, b, c):

    for i in range (len(a)):
        if a[i] != b[i]:
            c = 1
            break
    if c == 0:
        print("같다")
    else:
        print("다르다")

a = "xyz"
b = input()
c = 0

if len(a) == len(b):
    c = test_function(a, b, c)
else:
    print("다르다")

def add(x, y):
    a = x + y
    print ("%d + %d = %d" % (x, y, a))
def sub(x, y):
    a = x - y
    print ("%d - %d = %d" % (x, y, a))
def mul(x, y):
    a = x * y
    print ("%d * %d = %d" % (x, y, a))
def div(x, y):
    a = x // y
    print ("%d // %d = %d" % (x, y, a))

b = 3

while True:
    a = int(input("Enter the number: "))
    if a == 1:
        add(a, b)
    elif a == 2:
        sub(a, b)
    elif a == 3:
        mul(a, b)
    elif a == 4:
        div(a, b)
    elif a == 10:
        break

def test(a):

    a = a + 10

    print("in function is a", a)

    return a

a = 1

print ('out a is', a)

test(a)

print("out a is 2", a)

def game_369():
    for i in range(1, 100):
        a = i % 10
        b = i // 10

        if a % 3 == 0 and b % 3 == 0:
            print("**")
        elif a % 3 == 0 or b % 3 == 0:
            print("*")
        else:
            print(i)

game_369()
'''
def mul(a, b, i):

   while a != 10:

        c = i + 1
        d = 1

        while b != 10:
            c = i + 1
            print ("%d * %d = %d" % (a, b , a * b))

a = int(input("Enter the Number: "))
b = int(input("Enter the Number: "))
i = 0
mul(a, b, i)
'''
data type
int(정수), str(문자), float (소수), bool(T/F)
variable 변수
mod + - * / // %
'

#짝수홀수
a = int(input())

if a % 2 == 0:
    print("짝수")
elif a % 2 != 0:
    print("홀수")

if 0:
    print("HI")

for i in range(100):
    one = i % 10
    ten = i // 10
    if (ten == 3 or ten == 6 or ten == 9) and (one == 3 or one == 6 or one == 9):
        print("**")
    elif (one == 3 or one == 6 or one == 9) or (ten == 3 or ten == 6 or ten ==9):
        print("*")
    else:
        print(i)

a = int(input())

if a == 2:
    print("소수")
else:
    flag = 0
    for i in range(2, a):
        if a % i:
            flag = 1
    if flag == 0:
        print("소수")
    else:
        print("소수아님")

a = input()
b = a
flag = 0
for i in range(len(a)):
    if a[i] != b[len(a) - 1 - i]:
        flag = 1
        break
if flag == 1:
    print("different")
else:
    print("same")

#dictionary
a = {}
a['key'] = "value"
a['name'] = 'cat'
print(a['name'])
'''
a = int(input())
start = 1
end = 100

def count():
    for i in range(100):
        mid = (start+end)//2
        if mid == a:
            print('count', count)
        elif mid > a:
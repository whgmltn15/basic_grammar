'''
change = int(input())
coins = [500, 100, 50, 10]
a = []
for coin in coins:
    while change >= coin:
        change = change - coin
        a.append(coin)
print(a)
'''
#피보나치 수열
n = int(input())
a = [1, 2]
for i in range(1, n):
    if i > 1:
        a.append(a[i-1] + a[i-2])
print(a[len(a)-1])
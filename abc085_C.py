# -*- coding:utf-8 -*-

n, y = map(int,input().split())

a, b, c = 0, 0, 0

a = y // 10000
y = y % 10000
n -= a

b = y // 5000
y = y % 5000
n -= b

c = y // 1000
y = y % 1000
n -= c

if n < 0:
    print(-1, -1, -1)
elif n == 0:
    print(a,b,c)
elif (n + 1) % 5 == 0:
    print(a,b,c,n)
    print('test')
else:
    print(a,b,c,n)
    print('test')

#! -*- coding:utf-8 -*-

n = int(input())

a = []
b = []
for i in range(n):
    x,y = map(int,input().split())
    a.append(x)
    b.append(y)

x = min(a)
y = min(b)

a.sort()
b.sort(reverse = True)

print(a[-1] - a[0] + a[0] + b[-1])

# -*- coding:utf-8 -*-

n,q = map(int,input().split())

l = []
r = []
t = []

for i in range(q):
    a,b,c = map(int, input().split())
    l.append(a)
    r.append(b)
    t.append(c)

a = [0]*n

for i in range(q):
    for j in range(l[i]-1,r[i]):
        a[j] = t[i]

for i in range(n):
    print(a[i])

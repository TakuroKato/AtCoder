#! -*- coding:utf-8 -*-
N,W = map(int,input().split())
w = [0]*N
v = [0]*N
for i in range(N):
    w[i],v[i] = map(int,input().split())

x = [0]*N

for i in range(N):
    x[i] = v[i]/w[i]

total = 0
for i in range(N):
    tmp = max(x)
    k = x.index(tmp)
    x.pop(k)

    if W >= w[k]:
        total += v[k]
        W -= w[k]

print(total)

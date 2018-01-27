# -*- coding:utf-8 -*-
n,m,l = map(int,input().split())
r = float(m/l)
a,b,c = [],[],[]
for i in range(n):
    tmp = input().split()
    a.append(int(tmp[0]))
    b.append(int(tmp[1]))
    c.append(int(tmp[2]))

S = [0] * n
cost = [0] * n
x = []
def com():
    for i in range(n):
        S[i] = 0
        rec(0)
        
def rec(i):
    if i == n-1:
        print(S,c)
        x.append(S)
        return x

    rec(i+1)
    S[i] = 1
    cost[i] = c[i]
    rec(i+1)
    S[i] = 0
com()
print(x)

#! -*- coding:utf-8 -*-
N,T = map(int,input().split())
t = input()

t = t.split()
for i in range(len(t)):
    t[i] = int(t[i])

total = 0
for i in range(len(t)-1):
    if t[i+1] - t[i] >= T:
        total += T
    else:
        total += t[i+1] - t[i]
total += T
print(total)

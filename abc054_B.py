# -*- coding:utf-8 -*-
n,m = map(int,input().split())
a = []
for i in range(n):
    a.append(str(input()))
b = []
for i in range(m):
    b.append(str(input()))

f = [0]*m
tmp = []
for j in range(m):
    f[j] = a[j].find(b[j])
    if f[j] != -1:
        tmp.append(j)
while -1 in f: f.remove(-1)

try:
    if len(f) == 0:
        print('No')
    else:
        count = 0
        for i in range(len(tmp)):
            count += 1
            if (b[tmp[i]] in a[tmp[i]]) == False:
                count = 0
        if count == m:
            print('Yes')
        else:
            print('No')
except:
    print('No')

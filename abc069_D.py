#! -*- coding:utf-8 -*-
h,w = map(int,input().split())
n = int(input())
a = list(map(int,input().split()))

x = []
t = 1
for i in range(len(a)):
    for j in range(a[i]):
        x.append(t)
    t += 1

for i in range(h):
    for j in range(w):
        print(x[w*i + j],end= '')
        if j != w-1:
            print(' ',end = '')
    print('')

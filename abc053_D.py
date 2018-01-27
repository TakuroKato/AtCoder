# -*- coding:utf-8 -*-
n = int(input())
a = list(map(int,input().split()))
a.sort()
arr= []
count = 0
for i in range(len(a)):
    if a[i] == a[i-1]:
        arr.append(a[i])
        count += 1
if n-count-(count%2) <= 0:
    print(1)
else:
    print(n-count-(count%2))

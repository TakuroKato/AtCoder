#! -*- coding:utf-8 -*-
n = int(input())
a = list(map(int,input().split()))
arr = []
count = 0
for i in range(len(a)):
    if a[i] <= 3199:
        arr.append(a[i] // 400)
    else:
        count += 1
if len(set(arr)) != 0:
    print(len(set(arr)), len(set(arr)) + count,sep = ' ')
else:
    print(1, count,sep = ' ')

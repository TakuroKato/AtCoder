# -*- coding:utf-8 -*-
n,k = map(int,input().split())
a = list(input().split())
for i in range(len(a)):
    a[i] = int(a[i])
a = sorted(a)
sum = 0
count = 0
for i in range(k):
    sum += a[i] + count
    count += 1
print(sum)

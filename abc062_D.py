# -*- coding:utf-8 -*-
n = int(input())

a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])


s = n*3//2
d = []
for i in range(s):
    d.append(a[i])
arr1 = sorted(d)
print(arr1)

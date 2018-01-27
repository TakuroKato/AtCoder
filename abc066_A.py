#! -*- coding:utf-8 -*-
arr = input().split()
for i in range(len(arr)):
    arr[i] = int(arr[i])
arr.sort()

s = 0
for i in range(2):
    s += arr[i]

print(s)

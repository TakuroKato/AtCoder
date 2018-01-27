# -*- coding:utf-8 -*-

n = int(input())
arr = [['']*n]*n

for i in range(n):
    arr[i] =list(input())

for i in range(n):
    for j in range(n):
        print(arr[-1-j][i],end = '')
    print('')

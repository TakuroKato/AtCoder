#! -*- coding:utf-8 -*-

n = int(input())

n = str(n)
n = list(n)

flag = 0
for i in range(len(n)//2):
    if n[i] == n[-(i+1)]:
        pass
    else:
        flag = 1

if flag == 0:
    print('Yes')
else:
    print('No')

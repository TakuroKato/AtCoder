#! -*- coding:utf-8 -*-
n,m = map(int,input().split())
x = input().split()
for i in range(len(x)):
    x[i] = int(x[i])
y = input().split()
for i in range(len(y)):
    y[i] = int(y[i])

area = [[0] * (m-1)] * (n-1)
for i in range(n-1):
    for j in range(m-1):
        area[i][j] = (x[i+1] - x[i]) * (y[j+1] - y[j])
print(area)

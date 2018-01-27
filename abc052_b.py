# -*- coding:utf-8 -*-
x = 0
n = int(input())
s = str(input())
s = list(s)
data = []
for i in range(n):
    if s[i] == 'I':
        x += 1
    elif s[i] == 'D':
        x = x-1
    data.append(x)
m = max(data)
if m > 0:
    print(m)
else:
    print(0)

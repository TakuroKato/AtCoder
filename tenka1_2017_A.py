#! -*- coding:utf-8 -*-
s = list(input())

x = 0
for i in range(len(s)):
    k = int(s[i])
    if k == 1:
        x += 1

print(x)

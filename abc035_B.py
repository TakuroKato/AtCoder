# -*- coding:utf-8 -*-
import math

s = str(input())
t = int(input())

x = 0
y = 0
s = list(s)

h = 0

for i in range(len(s)):
    if s[i] == 'L':
        x -= 1
    if s[i] == 'R':
        x += 1
    if s[i] == 'U':
        y += 1
    if s[i] == 'D':
        y -= 1

    if s[i] =='?':
        if t == 1:
            h += 1
        elif t == 2:
            h -= 1
print(int(math.fabs(x) + math.fabs(y) + h))

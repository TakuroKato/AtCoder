# -*- coding:utf-8 -*-
s = list(input())

sum = 0
h = len(s)-1
for i in range(len(s)):
    if s[i] == 'U':
        sum += h - i
        sum += 2 * i 
    if s[i] == 'D':
        sum += 2 * (h - i)
        sum += i
print(sum)

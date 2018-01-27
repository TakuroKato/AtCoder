# -*- coding:utf-8 -*-
s = str(input())
s = list(s)
for i in range(len(s)):
    if s[i] == 'A':
        a = i
        break

for j in range(len(s)):
    if s[-j-1] == 'Z':
        z = j
        break
print((len(s)-j)-i)

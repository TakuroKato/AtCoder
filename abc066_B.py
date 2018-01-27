#! -*- coding:utf-8 -*-
s = str(input())
s = list(s)
#print(s)
a = 'x'
b = 'x'

for i in range(len(s)):
    s.pop()
    if len(s) % 2 == 0:
        a = s[:len(s)//2]
        b = s[len(s)//2:]
        if a == b:
            print(len(s))
            break

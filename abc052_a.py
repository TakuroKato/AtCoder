# -*- coding:utf-8 -*-

a,b,c,d = map(int,input().split())
s1 = a*b
s2 = c*d
if s1 >= s2:
    print(s1)
else:
    print(s2)

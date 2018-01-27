#! -*- coding:utf-8 -*-
a,b,c,d = map(int,input().split())
if d <= a or b <= c:
    print(0)
elif c <= a and (a <= d and d <= b):
    print(d-a)
elif (a <= c and c <= b) and (a <= d and d <= b):
    print(d-c)
elif (a <= c and c <= b) and b <= d:
    print(b-c)
else:
    print(b-a)

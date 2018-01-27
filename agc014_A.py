#! -*- coding:utf-8 -*-
a,b,c = map(int,input().split())

count = 0
flag = 0
while True:
    at = (b+c)/2
    bt = (a+c)/2
    ct = (b+a)/2

    if flag == 0 and (a % 2 == 1 or b % 2 == 1 or c % 2 == 1):
        flag = 1
        break
    if flag == 1 and at == a and bt == b and ct == c:
        flag = 0
        break
    
    a = at
    b = bt
    c = ct
    #print(a,b,c)
    count += 1
    flag = 1
    if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
        break

if flag == 0:
    print(-1)
else:
    print(count)

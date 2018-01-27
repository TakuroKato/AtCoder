#! -*- coding:utf-8 -*-
a,b,c = map(int,input().split())

if c == 0:
    print('YES')
elif a == 1:
    print('YES')
elif b == 1:
    if c == 0:
        print('YES')
    else:
        print('NO')
elif a % 2 == 0 and b % 2 == 0 and c % 2 == 1:
    print('NO')    
elif a % 2 == 1 and b % 2 == 0 and c % 2 == 0:
    print('NO')
elif a % 2 == 0 and b % 2 == 1 and c % 2 == 1:
    print('NO')
else:
    print('YES')

# -*- coding:utf-8 -*-
a = [1,3,5,7,8,10,12]
b = [4,6,9,11]
c = [2]

x, y = map(int,input().split())

flag = 0
for i in range(len(a)):
    if a[i] == x:
        flag = 1

for i in range(len(b)):
    if b[i] == x:
        flag = 2

for i in range(len(c)):
    if c[i] == x:
        flag = c

result = 0        
if flag == 1:
    for i in range(len(a)):
        if a[i] == y:
            result = 1
elif flag == 2:
    for i in range(len(b)):
        if b[i] == y:
            result = 1
elif flag == 3:
    for i in range(len(c)):
        if c[i] == y:
            result = 1

if result == 1:
    print('Yes')
elif result == 0:
    print('No')
    

#! -*- coding:utf-8 -*-
s = str(input())
s = list(s)
x = 'abcdefghijklmnopqrstuvwxyz'
x = list(x)

flag = 0
for i in range(len(s)):
    try:
        if(len(x) == 1 and s[i] == x[0]):
            flag = 1
        x.remove(s[i])
    except:
        pass

if(flag == 1):
    print('None')
else:
    print(x[0])

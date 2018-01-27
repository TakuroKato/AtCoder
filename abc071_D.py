#! -*- coding:utf-8 -*-
n = int(input())
s1 = list(map(str,list(input())))
s2 = list(map(str,list(input())))

flag = 0
a = 0

x = 1
for i in range(n):
    if a == 1:
        a = 0
    elif flag == 0 and s1[i] == s2[i]:
        x *= 3
        flag = 1
    elif flag == 0 and s1[i] != s2[i]:
        x *= 3 * 2
        a = 1
        flag = 2
    elif flag == 1 and s1[i] == s2[i]:
        x *= 2
        flag = 1
    elif flag == 1 and s1[i] != s2[i]:
        x *= 2 * 1
        a = 1
        flag = 2
    elif flag == 2 and s1[i] == s2[i]:
        x *= 1
        flag = 1
    elif flag == 2 and s1[i] != s2[i]:
        x *= 3
        a = 1
        flag = 2
print(x%1000000007)

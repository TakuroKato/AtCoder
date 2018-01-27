#-*- coding:utf-8 -*-
s = str(input())
s = s.rsplit(',')
for i in range(len(s)-1):
    print(s[i], end = ' ')
print(s[len(s)-1])

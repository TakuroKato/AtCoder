#! -*- coding:utf-8 -*-
n = int(input())
a = map(int,input().split())
a = list(a)
a = sorted(a,reverse=True)

x = 0
tmp = 0
for i in range(len(a)):
    #print(a)
    #print(tmp,a[0])
    if tmp == a[0]:
        x = a[0]
        a.remove(a[0])
        break
    else:
        tmp = a[0]
        a.remove(a[0])

b = 0
tmp = 0
for i in range(len(a)):
    if tmp == a[0]:
        b = a[0]
        break
    else:
        tmp = a[0]
        a.remove(a[0])

#print(x)
#print(b)
print(x*b)

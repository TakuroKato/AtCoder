#! -*- coding:utf-8 -*-
n = int(input())
a = map(int,input().split())
a = list(a)
x = []
#a = []
#for i in range(200000):
#    a.append(i)

count = 0
for i in range(n):
    if count % 2 == 1:
        x.append(a[i])
    else:
        x.insert(0,a[i])

    count += 1

if n % 2 == 0:
    x.reverse()
    x = map(str,x)
    print(' '.join(x))

else:
    x = map(str,x)
    print(' '.join(x))

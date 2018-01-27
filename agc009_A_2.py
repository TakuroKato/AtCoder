# -*- coding:utf-8 -*-
n = int(input())
a = [0]*n
b = [0]*n

for i in range(n):
    a[i],b[i] = map(int,input().split())
a.reverse()
b.reverse()
count = 0
for i in range(n):
    if (a[i]+count)%b[i] == 0:
        pass
    elif a[i]+count > b[i]:
        count += (b[i]*(((a[i]+count)//b[i])+1))-(a[i]+count)
    else:
        count += b[i] - (a[i]+count)
print(count)

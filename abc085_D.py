# -*- coding:utf-8 -*-

n, h = map(int, input().split())
a = []
b = []

for i in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

a.sort()
b.sort()

x = a[-1]

count = 0
while(h > 0):    
    if b[-1] > x:
        h -= b.pop()
        count += 1;
        if not b:
            b.append(-100)
    else:
        #h -= a[-1]
        #count += 1;
        count += (h // a[-1])
        h -= a[-1] * (h//a[-1])
        break
if h > 0:
    count += 1
print(count)

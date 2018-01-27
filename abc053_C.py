# -*- coding:utf-8 -*-
x = int(input())
k = 2*(x//(5+6))
r,tmp = x%(5+6),x%(5+6)
count = 0
while True:
    r -= 6-(count%2)
    if r <= 0:
        break
    count += 1
if x <= 6:
    print(1)
elif tmp == 0:
    print(k)
else:
    print(count+k+1)

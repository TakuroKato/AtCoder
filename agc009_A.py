# -*- coding:utf-8 -*-
import numpy as np
def button(t):
    tmp = [1]*(t+1)
    tmp2 = [0]*(n-t-1)
    tmp3 = tmp+tmp2
    tmp3 = np.array(tmp3)
    global a
    a = a+tmp3
    return 0

n = int(input())
global a
a = [0]*n
b = [0]*n

for i in range(n):
    a[i],b[i] = map(int,input().split())
a = np.array(a)

count = 0
for i in range(n):
    while True:
        if a[n-1-i] % b[n-1-i] == 0:
            break
        else:
            button(n-1-i)
            count += 1

print(count)

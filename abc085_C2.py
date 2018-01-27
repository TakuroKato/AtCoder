# -*- coding:utf-8 -*-
import sys

n, y = map(int,input().split())

a, b, c = 0, 0, 0

am = y // 10000
bm = y // 5000
cm = y // 1000

for i in range(am+1):
    for j in range(bm+1):
        if (9000*i + 4000*j + 1000*n == y) and (n-i-j >= 0):
            print(i, j ,n-i-j)
            sys.exit()
        if (y - 1000*n - 4000*j < 0):
            break
        if (n-i-j < 0):
            break

print(-1,-1,-1)

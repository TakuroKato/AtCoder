# -*- coding:utf-8 -*-
n, m = map(int, input().split())

k = m // 2
r = m % 2
if n >= k:
    print(k)
else:
    print(n + (k-n) // 2)

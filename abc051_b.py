# -*- coding:utf-8 -*-
n = input()
n = n.split()
K,S = map(int, n)

count = 0
for x in range(K+1):
    for y in range(K+1):
        for z in range(K+1):
            if x+y+z == S:
                count += 1
print(count)

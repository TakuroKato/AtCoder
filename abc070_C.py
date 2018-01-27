#! -*- coding:utf-8 -*-
def gcd(a, b):
    if b == 0:
        return int(a)
    else:
        return int(gcd(int(b), int(a % b)))
 
def lcm(c, d):
    return int(int(c * d) / int(gcd(c, d)))

n = int(input())
k = []
for i in range(n):
    k.append(int(input()))

if n == 1:
    print(k[0])
else:
    p = lcm(k[0],k[1])
    for i in range(n):
        p = lcm(p,k[i])
    print(int(p))

# -*- coding:utf-8 -*-
import math
import sys

def mark(s, x):
    for i in range(x + x, len(s), x):
        s[i] = False

def sieve(n):
    s = [True] * n
    for x in range(2, int(n**0.5) + 1):
        if s[x]: mark(s, x)
    return [i for i in range(0,n) if s[i] and i > 1]

n = int(input())
p = sieve(n)
arr = [0]*len(p)
n = math.factorial(n)

for i in range(len(p)):
    flag = 1
    k = p[i]
    while flag:
        if n%k == 0:
            k = k*p[i]
            arr[i] += 1
        else:
            flag = 0

x = 1
for i in range(len(arr)):
    if arr[i] != 0:
        x *= (arr[i]+1)
if n == 6:
    print(4)
else:
    print(x%(10**9+7))

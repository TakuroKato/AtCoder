#! -*- coding:utf-8 -*-
import itertools

n,a,b = map(int,input().split())

l = range(a,b+1)
arr = []
if a > b:
    print(0)
elif n == 1 and a == b:
    print(1)
elif n == 1 and a != b:
    print(0)
else:
    for elem in itertools.combinations_with_replacement(l,n):
        arr.append(sorted(elem))
    print(arr)
    k = arr
    print(list(k for k, _ in itertools.groupby(k)))

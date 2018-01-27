#! -*- coding:utf-8 -*-
import sys

n = int(input())

if n % 4 == 0:
    print(3*(n//4),3*(n//4),3*(n//4))
elif n % 4 == 2:
    print(2*(n//4)+1,2*(2*(n//4)+1),2*(2*(n//4)+1))
else:
    for i in range(1,3501):
        for j in range(1,i+1):
            for k in range(1,j+1):
                if 4/n == 1/i + 1/j + 1/k:
                    print(i,j,k)
                    sys.exit()

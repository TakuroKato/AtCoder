#! -*- coding:utf-8 -*-
n = int(input())
a = map(int,input().split())
a = list(a)

sum_2 = 0
sum_4 = 0
for i in range(len(a)):
    if a[i] % 4 == 0:
        sum_4 += 1
    elif a[i] % 2 == 0:
        sum_2 += 1

if len(a)//2 == sum_4 or (len(a)+1)//2 == sum_4:
    print('Yes')
elif sum_4*2 + sum_2 >= len(a):
    print('Yes')
else:
    print('No')

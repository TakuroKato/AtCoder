#! -*- coding:utf-8 -*-
x,a,b = map(int,input().split())
import math

if(math.copysign(x-a,0) < math.copysign(x-b,0)):
    print('A')
else:
    print('B')

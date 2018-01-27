# -*- coding:utf-8 -*-
h,w = map(int,input().split())
arr = []
for i in range(h):
    arr.append(input())


for i in range(w+2):
    print('#',sep = '',end = '')
print('')

for i in range(h):
    print('#',sep = '',end = '')
    print(arr[i],sep = '',end = '')
    print('#')

for i in range(w+2):
    print('#',sep = '',end = '')
print('')    

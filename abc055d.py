# -*- coding:utf-8 -*-
n = int(input())
s = list(str(input()))
arr1 = ['S']*n
arr2 = ['S']*n
arr2[1] = 'W'
arr3 = ['S']*n
arr3[0] = 'W'
arr3[1] = 'W'
arr4 = ['S']*n
arr4[0] = 'W'

flag = 0
for i in range(1,n):
    if arr1[i] == 'S' and s[i] == 'o':
        if arr1[i-1] == 'S':
            arr1[(i+1)%n] = 'S'
        else:
            arr1[(i+1)%n] = 'W'
    elif arr1[i] == 'S' and s[i] == 'x':
        if arr1[i-1] == 'S':
            arr1[(i+1)%n] = 'W'
        else:
            arr1[(i+1)%n] = 'S'        
    if arr1[i] == 'W' and s[i] == 'o':
        if arr1[i-1] == 'S':
            arr1[(i+1)%n] = 'W'
        else:
            arr1[(i+1)%n] = 'S'
    elif arr1[i] == 'W' and s[i] == 'x':
        if arr1[i-1] == 'S':
            arr1[(i+1)%n] = 'S'
        else:
            arr1[(i+1)%n] = 'W'

for i in range(1,n):
    if arr4[i] == 'S' and s[i] == 'o':
        if arr4[i-1] == 'S':
            arr4[(i+1)%n] = 'S'
        else:
            arr4[(i+1)%n] = 'W'
    elif arr4[i] == 'S' and s[i] == 'x':
        if arr4[i-1] == 'S':
            arr4[(i+1)%n] = 'W'
        else:
            arr4[(i+1)%n] = 'S'        
    if arr4[i] == 'W' and s[i] == 'o':
        if arr4[i-1] == 'S':
            arr4[(i+1)%n] = 'W'
        else:
            arr4[(i+1)%n] = 'S'
    elif arr4[i] == 'W' and s[i] == 'x':
        if arr4[i-1] == 'S':
            arr4[(i+1)%n] = 'S'
        else:
            arr4[(i+1)%n] = 'W'
            
print(arr1)
print(arr4)

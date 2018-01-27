# -*- coding:utf-8 -*-
n = int(input())
a = [[0]*n]*n
check = ['#']*n
check2 = ['.']*n

for i in range(n):
    tmp = input()
    a[i] = list(tmp)

flag = 0
flag2 = 0
for i in range(n):
    if a[i] != check:
        flag = 1
        break
for i in range(n):
    if a[i] != check2:
        flag2 = 1
        break

if flag == 0:
    print(0)
elif flag2 != 1:
    print(-1)
else:
    m = 0
    c = []
    tmpi = 0
    count = 0
    for i in range(n):
        if m < a[i].count('#'):
            m = a[i].count('#')
            count += 1
            tmpi = i
    for i in range(n):
        flag = 0
        for j in range(n):
            if a[j][i] != '#':
                flag = 1
                break
        if flag == 0:
            c.append(i)
    if m == n:                
        print(m-len(c))
        
    elif m == 1 and count == 1:
        if tmpi != a[tmpi].index('#'):
            for i in range(n):
                flag = 0
                for j in range(n):
                    if a[i][j] == '#':
                        if i == j:
                            print(n-1+n-len(c))
                            flag = 1
                            break
                if flag == 1:
                    break
            if flag == 0:
                print(2*n)
        else:
            print(n-m+n-len(c))

    else:
        flag = 0
        for i in range(n):
            if a[i] == '#.#':
                print(6)
                flag = 1
                break
        if flag == 0:
            ad = n-m
            print(ad + n - len(c))

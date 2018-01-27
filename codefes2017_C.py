#! -*- coding:utf-8 -*-
import collections
H,W = map(int,input().split())

arr = [[0]*W]*H

for i in range(H):
    arr[i] = list(input())
    
if H == 1 and W == 1:
    print('Yes')
elif H == 1 or W == 1:
    stock = []
    count = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] in stock:
                count += 1
                stock.remove(arr[i][j])
            else:
                stock.append(arr[i][j])

    if H == 1 and W%2 == 0:
        if count == W//2:
            print('Yes')
        else:
            print('No')
    elif H == 1 and W%2 == 1:
        if count == W//2:
            print('Yes')
        else:
            print('No')
    elif W == 1 and H%2 == 0:
        if count == H//2:
            print('Yes')
        else:
            print('No')
    elif W == 1 and H%2 == 1:
        if count == H//2:
            print('Yes')
        else:
            print('No')
            
else:
    li = [ y for x in arr for y in x]
    count_dict = collections.Counter(li)
    if H%2 == 0 and W%2 == 0:
        flag = 0
        for k,v in count_dict.items():
            if v%4 != 0:
                flag = 1

        if flag == 0:
            print('Yes')
        else:
            li_uniq = list(set(li))
            if len(li_uniq) == 1:
                print('Yes')
            else:
                print('No')
                
    elif H%2 == 1 and W%2 == 1:
        flag1 = 0
        flag2 = 0
        flag3 = 0
        for k,v in count_dict.items():
            if v%4 != 0:
                if v % 2 == 0:
                    flag2 += 1
                elif v % 2 == 1:
                    flag3 += 1
                else:
                    flag1 = 1
        #print(flag1,flag2,flag3)
        if (flag1 == 0 and flag2 == 2 and flag3 == 1) or (flag1 == 0 and flag2 == 0 and flag3 == 1) or (flag1 == 0 and flag2 == 3 and flag3 == 1) or (flag1 == 0 and flag2 == 1 and flag3 == 1):
            print('Yes')
        else:
            li_uniq = list(set(li))
            if len(li_uniq) == 1:
                print('Yes')
            else:
                print('No')

    else:
        flag1 = 0
        flag2 = 0
        for k,v in count_dict.items():
            if v%4 != 0:
                if v % 4 == 2:
                    flag2 += 1
                else:
                    flag1 = 1
        #print(flag1,flag2)
        if H%2 == 1:
            x = W//2
        elif W%2 == 1:
            x = H//2
        if (flag1 == 0 and flag2 == x):
            print('Yes')
        else:
            li_uniq = list(set(li))
            if len(li_uniq) == 1:
                print('Yes')
            else:
                print('No')

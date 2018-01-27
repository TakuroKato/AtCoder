# -*- coding:utf-8 -*-
n,k = map(int,input().split())
a = list(input().split())
s = []
for i in range(n):
    s.append(str(input()))

m = 10
mi = ''
for i in range(len(a)):
    if len(list(s[int(a[i])-1])) < m:
        m = len(s[int(a[i])-1])
        mi = s[int(a[i])-1]

if n == k:
    print('')
else:
    data = []
    for i in range(len(a)):
        data.append(s[int(a[i])-1])

    common = []
    flag = 0
    for i in range(len(mi)):
        if flag == 0:
            for j in range(len(data)):
                tmp = data[j]
                tmp = list(tmp)
                if tmp[i] != mi[i]:
                    flag = 1
                    break
        if flag == 0:
            common.append(mi[i])
    m = len(common)

    if len(common) == 0:
        print(-1)
    else:
        count = 0
        for i in range(len(s)):
            tmp = list(s[i])
            if tmp[0:m] == common:
                count += 1

        if count == len(a):
            flag = 0
            le = []
            for i in range(len(common)):
                if flag == 0:
                    for j in range(len(s)):
                        tmp = list(s[j])
                        try:
                            if tmp[i] != common[i]:
                                flag = 1
                                le.append(common[i])
                                break

                        except:
                            pass
                    if flag == 0:
                        le.append(common[i])
            print("".join(le))
        else:
            print(-1)

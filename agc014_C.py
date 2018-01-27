#! -*- coding:utf-8 -*-
h,w,k = map(int,input().split())
a = []
for i in range(h):
    a.append(list(input()))

for i in range(h):
    for j in range(w):
        if a[i][j] == 'S':
            si = i
            sj = j
            break

if (si - 1 == 0 and a[si-1][sj] == '.') or (sj - 1 == 0 and a[si][sj-1] == '.') or (si + 1 == h-1 and a[si+1][sj] == '.') or (sj + 1 == w-1 and a[si][sj+1] == '.'):
    print(1)
else:
    u,d,l,r = [],[],[],[]
    for i in range(h):
        if a[i][sj] == '#':
            if i <= si:
                u.append('#')
            else:
                d.append('#')
        else:
            if i <= si:
                u.append('.')
            else:
                d.append('.')
        
    for j in range(w):
        if a[si][j] == '#':
            if j <= sj:
                l.append('#')
            else:
                r.append('#')
        else:
            if j <= sj:
                l.append('.')
            else:
                r.append('.')
    u.pop()
    u.reverse()
    l.pop()
    l.reverse()
    
    print(u,l,d,r)
    
    vu = 0
    while True:
        if u == []:
            break
        q = 0
        for i in range(k):
            try:
                if u[i-q] == '.':
                    u.pop(0)
                    q += 1
                else:
                    break
            except:
                pass
        count = 0
        for i in range(len(u)):
            if u[i] == '#':
                u[i] = '.'
                count += 1
            if count == k:
                break
        vu += 1

    vl = 0
    while True:
        if l == []:
            break
        q = 0
        for i in range(k):
            try:
                if l[i-q] == '.':
                    l.pop(0)
                    q += 1
                else:
                    break
            except:
                pass
        count = 0
        for i in range(len(l)):
            if l[i] == '#':
                l[i] = '.'
                count += 1
            if count == k:
                break
        vl += 1
        
    vd = 0
    while True:
        if d == []:
            break
        q = 0
        for i in range(k):
            try:
                if d[i-q] == '.':
                    d.pop(0)
                    q += 1
                else:
                    break
            except:
                pass
        count = 0
        for i in range(len(d)):
            if d[i] == '#':
                d[i] = '.'
                count += 1
            if count == k:
                break
        vd += 1        

    vr = 0
    while True:
        #print('---')
        #print(r)
        if r == []:
            break
        q = 0
        for i in range(k):
            try:
                if r[i-q] == '.':
                    r.pop(0)
                    q += 1
                else:
                    break
            except:
                pass
        count = 0
        #print(r)
        for i in range(len(r)):
            if r[i] == '#':
                r[i] = '.'
                count += 1
            if count == k:
                break
        vr += 1
        #print(r)

        
        
    #print(vu,vl,vd,vr)

    print(min(vu,vl,vd,vr))

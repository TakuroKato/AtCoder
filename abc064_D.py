#! coding:utf-8 -*-
n = int(input())
s = input()
s = list(s)

count = 0
k = 0
ans = []
ls = 's'
for i in range(len(s)):
    if (ls == 's' and s[i] == '(') or (ls == '(' and s[i] == '('):
        count += 1
        ls = '('
    elif s[i] == ')':
        k += 1
        ls = ')'
    elif ls == ')' and s[i] == '(':
        if k - count > 0: 
            for i in range(k - count):
                ans.insert(0,'(')
            for i in range(count):
                ans.append('(')
            for i in range(k):
                ans.append(')')
        else :
            for i in range(count):
                ans.append('(')
            for i in range(k):
                ans.append(')')
            for i in range(k - count):
                ans.append(')')

        k = 0
        count = 1



if k - count > 0: 
    for i in range(k - count):
        ans.insert(0,'(')
    for i in range(count):
        ans.append('(')
    for i in range(k):
        ans.append(')')
else :
    for i in range(count):
        ans.append('(')
    for i in range(k):
        ans.append(')')
    for i in range(k - count):
        ans.append(')')


tmp = 0
for i in range(len(ans)):
    if ans[-1 - i] == '(':
        tmp += 1
    else:
        break

for i in range(tmp):
    ans.append(')')

for i in range(len(ans)):
    print(ans[i],sep = '', end = '')
print()

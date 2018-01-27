#! -*- coding:utf-8 -*-
import itertools

l = range(1,6)

#リストlから要素を３つ選んで並べる
#重複は考慮せず，順序のみ考慮する
#要するに順列を求める
p = []
for x in itertools.permutations(l,3):
    p.append(x)
print(p)
print(len(p))

#リストlから要素を２つ選んで並べる
#重複，順序ともに考慮しない
#要するに組み合わせを求める
c = []
for x in itertools.combinations(l,3):
    c.append(x)
print(c)
print(len(c))

#デカルト積（直積）を求める
dp = []
for elem in itertools.product(l, repeat = 2):
    dp.append(elem)
print(dp)
print(len(dp))


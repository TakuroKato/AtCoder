#! -*- coding:utf-8 -*-
def member(self, x):
    cp = self.top.next
    while cp:
        if cp.item == x: return True
        cp = cp.next
    return False

class Set:
    class Cell:
        def __init__(self, x, next = None):
            self.item = x
            self.next = next
    
    def __init__(self, data = None):
        self.top = Set.Cell(None)   # Header Cell
        if data:
            for x in data:
                if not self.member(x):
                    self.top.next = Set.Cell(x, self.top.next)

def insert(self, x):
    if not self.member(x):
        self.top.next = Set.Cell(x, self.top.next)

def issubset(self, x):
    cp = self.top.next
    while cp:
        if not x.member(cp.item): return False
        cp = cp.next
    return True

def isequal(self, x):
    return self.issubset(x) and x.issubset(self)

def union(self, x):
    def _union(cp):
        if cp is None: return x.top.next
        elif x.member(cp.item):
            return _union(cp.next)
        else:
            return Set.Cell(cp.item, _union(cp.next))

    s = Set()
    s.top.next = _union(self.top.next)
    return s

def intersection(self, x):
    def _intersection(cp):
        if cp is None: return None
        elif x.member(cp.item):
            return Set.Cell(cp.item, _intersection(cp.next))
        else:
            return _intersection(cp.next)

    s = Set()
    s.top.next = _intersection(self.top.next)
    return s

def remove(self, x):
    def _remove(cp):
        if cp is None: return None
        elif cp.item == x: return cp.next
        else: return Set.Cell(cp.item, _remove(cp.next))

    self.top.next = _remove(self.top.next)


if __name__ == '__main__':
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        x,y = map(int,input().split())
        a.append(x)
        b.append(y)

    #a = Set([1,2,3,4,5])
    #b = Set([4,5,6,7,8])
    a = Set(a)
    b = Set(b)
    print(a)
    print(b)
    c = a.union(b)
    print(c)
    d = a.intersection(b)
    print(d)
    e = a.difference(b)
    print(e)
    print(a.issubset(c))
    print(c.issubset(a))
    print(a.isequal(a))
    a.insert(1)
    print(a)
    a.insert(10)
    print(a)
    b.remove(5)
    print(b)
    print(c)

 

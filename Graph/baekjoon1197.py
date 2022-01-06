# [Gold 4] 최소 스패닝 트리
# 선을 선택한다 생각하지 말고 점을 선택한다 보면 좀 더 쉽다.
import sys

v, e = map(int, input().split())
edges = []
for _ in range(e):
    edges.append(list(map(int, input().split())))
edges.sort(key=lambda x:x[2])

parent = [i for i in range(v)] #기본 상태
def getParent(x):
    if (parent[x] == x):
         return x;
    else:
        return getParent(parent[x])

def unionParent(a, b):
    a = getParent(a)
    b = getParent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def findParent(a, b):
    a = getParent(a)
    b = getParent(b)
    if a == b:
        return True
    else:
        return False
total = 0
for a, b, value in edges:
    if not findParent(a - 1, b - 1):
        unionParent(a - 1, b - 1)
        total += value
print(total)
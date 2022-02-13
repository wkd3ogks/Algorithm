# [Gold 4] 도시 분할 계획

# 스패닝 트리에서 가장 큰 값 하나 짤라내면 끝.
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
edges = []
unionFind = [i for i in range(n)]
for _ in range(m):
    n1, n2, value = map(int, input().split())
    edges.append((n1 - 1, n2 - 1, value))
edges.sort(key=lambda x:x[2])

def getParent(x):
    if unionFind[x] == x:
        return x 
    return getParent(unionFind[x])

def unionParent(a, b):
    a = getParent(a)
    b = getParent(b)

    if a < b:
        unionFind[b] = a
    else:
        unionFind[a] = b

def findParent(a, b):
    a = getParent(a)
    b = getParent(b)
    if a == b:
        return True
    else:
        return False
big = 0
total = 0
for node1, node2, value in edges:
    if not findParent(node1, node2):
        if big < value:
            big = value
        unionParent(node1, node2)
        total += value
print(total - big)

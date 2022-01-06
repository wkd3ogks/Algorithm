# [Gold 3] 줄 세우기
# 그래프로 이 문제를 바라보자
# 위상정렬인데 사이클 체크할 필요가 없는.
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
memo = [0 for i in range(n + 1)]
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split()) 
    memo[b] += 1
    graph[a].append(b)
queue = deque([])
for i in range(1, n + 1):
    if memo[i] == 0:
        queue.append(i)
        memo[i] = -1
def removeEdges(a):
    rslt = []
    while graph[a]:
        b = graph[a].pop()
        memo[b] -= 1
        if memo[b] == 0:
            rslt.append(b)
    return rslt
while queue:
    x = queue.popleft()
    print(x, end=' ')
    for i in removeEdges(x):
        queue.append(i)

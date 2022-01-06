# [Gold 2] 문제집
# 위상 정렬문제(큐가 아닌 최소힙을 이용) 
import sys
import heapq

queue = []
input = sys.stdin.readline
n, m = map(int, input().split())
inDegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1
for i in range(1, n + 1):
    if inDegree[i] == 0:
        heapq.heappush(queue, i)

while queue:
    x = heapq.heappop(queue)
    print(x, end=' ')
    while graph[x]:
        b = graph[x].pop()
        inDegree[b] -= 1 
        if inDegree[b] == 0:
            heapq.heappush(queue, b)

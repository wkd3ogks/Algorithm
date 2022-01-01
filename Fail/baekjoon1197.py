# [Gold 4] 최소 스패닝 트리
# 벨만 포드 알고리즘은 뭐였드라?
# 벨만 포드 알고리즘과 다익스트라의 차이는 
import sys
from collections import deque

v, e = map(int, sys.stdin.readline().split())
# visitd .> [0, 0] first : total cost 
INF = 2147483647
visited = [[INF, node for _ in range(v)]
graph = [[] for _ in range(v)]
visited[0] = 0
mstEdges = set()
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    graph[a].append((b, c))
    graph[b].append((a, c))
queue = deque([0])
while queue:
    check = False
    node = queue.popleft()
    for nxtNode, value in graph[node]:
        if visited[nxtNode][1] < visited[node][1] + value:
            visited[nxtNode][1] = visited[node][1] + value
            mstEdges.add((node, nxtNode, value))
            if nxtNode not in mstEdges:
                mstEdges.add((node, nxtNode, value))
            else:
                mstEdges.remove((node, nxtNode, value))
                mstEdges.add((node, nxtNode, value))


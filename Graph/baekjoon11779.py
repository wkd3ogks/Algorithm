# [Gold 3] 최소 비용 구하기 2
 
import sys
import heapq
n = int(sys.stdin.readline()) 
m = int(sys.stdin.readline()) 
INF = 100000001
graph = [[] for _ in range(n)]
before = [-1 for _ in range(n)]
visited = [INF for _ in range(n)]
for _ in range(m):
    start, end, value = map(int, sys.stdin.readline().split())
    start -= 1
    end -= 1
    graph[start].append((end, value))
startNode, endNode = map(int, sys.stdin.readline().split())
heap = []
heapq.heappush(heap, (startNode - 1, 0))
visited[startNode - 1] = 0
while heap:
    node, length = heapq.heappop(heap)
    if visited[node] < length:
        continue
    for next, value in graph[node]:
        if visited[node] + value < visited[next]:
            before[next] = node
            visited[next] = visited[node] + value
            heapq.heappush(heap, (next, visited[next]))

before[startNode - 1] = -2
n = before[endNode - 1]
result = [endNode]
while n != -2:
    result.append(n + 1)
    n = before[n]
print(visited[endNode - 1])
print(len(result))
while result:
    print(result.pop(), end=' ')

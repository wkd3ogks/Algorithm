# [Gold 4] 서강그라운드
import sys
from collections import deque
n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]
items = list(map(int, sys.stdin.readline().split()))
total = 0
max = 0
def solve(start, cnt):
    global total
    for node, street in graph[start]:
        if visited[node] == 0 and street + cnt <= m:
            visited[node] = cnt + street 
            total += items[node]
            solve(node, cnt + street) 
        elif visited[node] > cnt + street and street + cnt <= m:
            visited[node] = cnt + street
            solve(node, cnt + street)

for i in range(r):
    start, end, street = map(int, sys.stdin.readline().split())
    graph[start - 1].append((end - 1, street))
    graph[end - 1].append((start - 1, street))
for start in range(n):
    total = items[start]
    visited = [0 for _ in range(n)]
    visited[start] = 1 
    solve(start, 0)
    if max < total:
        max = total
print(max)
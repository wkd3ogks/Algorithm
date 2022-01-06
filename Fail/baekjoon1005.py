# [Gold 3] ACM Craft
# 역순으로 하면 안된다!
import sys
input = sys.stdin.readline

def dfs(level, node):
    print(level, node)
    visited[node] = True
    if spand[level] < time[node - 1]:
        spand[level] = time[node - 1]
    for node2 in graph[node]:
        if visited[node2] == False:
            dfs(level + 1, node2)

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    time = list(map(int, input().split()))
    start = []
    spand = [0] * 1000
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
    w = int(input())
    dfs(0, w)
    total = 0
    for i in spand:
        total += i
    print(spand)
    print(total)

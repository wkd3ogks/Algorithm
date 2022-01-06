# [Gold 3] ACM Craft
# 역순으로 하면 안된다!
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    time = list(map(int, input().split()))
    start = []
    dp = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    inDegree = [0] * (n + 1)
    for _ in range(k):
        a, b = map(int, input().split())
        inDegree[b] += 1
        graph[a].append(b)
    w = int(input())
    queue = deque([])
    for i in range(1, n + 1):
        if inDegree[i] == 0:
            queue.append(i)
            dp[i] = time[i - 1]
    while queue:
        node = queue.popleft()
        while graph[node]:
            b = graph[node].pop()
            if dp[b] < dp[node] + time[b - 1]:
                dp[b] = dp[node] + time[b - 1]
            inDegree[b] -= 1
            if inDegree[b] == 0:
                queue.append(b)
    print(dp[w])

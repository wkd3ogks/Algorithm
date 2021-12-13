import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
visited = []
startNode = deque([(0,0),(m - 1, 0), (0, n - 1), (m - 1, n - 1)])
delta = [[(1, 0), (0, 1)], [(0, -1), (1, 0)], [(0, -1), (-1, 0)], [(0, 1), (-1, 0)]]
data = []
for i in range(n):
    data.append(sys.stdin.readline().rstrip().split())
    visited.append([])
    for j in range(m):
        visited[i].append(False)
time = 0
cnt = 0
change = []
while startNode:
    nowNode = startNode.popleft()
    check = False
    queue = deque()
    queue.append(nowNode)
    path = []
    while queue:
        print(queue)
        nodex, nodey = queue.popleft()
        for i in range(2):
            if 0 <= nodex + delta[cnt][i][0] <= m - 1 and 0 <= nodey + delta[cnt][i][1] <= n - 1:
                if visited[nodey + delta[cnt][i][1]][nodex + delta[cnt][i][0]] == False and data[nodey + delta[cnt][i][1]][nodex + delta[cnt][i][0]] == '0':
                    visited[nodey + delta[cnt][i][1]][nodex + delta[cnt][i][0]] = True
                    queue.append((nodex + delta[cnt][i][0], nodey + delta[cnt][i][1]))
                elif visited[nodey + delta[cnt][i][1]][nodex + delta[cnt][i][0]] == False and data[nodey + delta[cnt][i][1]][nodex + delta[cnt][i][0]] == '1':
                    visited[nodey + delta[cnt][i][1]][nodex + delta[cnt][i][0]] = True
                    change.append((nodex + delta[cnt][i][0], nodey + delta[cnt][i][1]))
    cnt += 1
print(change)


                
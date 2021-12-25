# [Gold 4] 알파벳
from collections import deque

r, c = map(int, input().split())
alphaMap = []
for i in range(r):
    alphaMap.append(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

rslt = 0

def dfs(x, y, visited, cnt):
    global rslt
    if rslt == 26:
        return
    if rslt < cnt:
        rslt = cnt
    for i in range(4):
        if 0 <= x + dx[i] and x + dx[i] < c and 0 <= y + dy[i] and y + dy[i] < r:
            nx = x + dx[i]
            ny = y + dy[i]
            index = ord(alphaMap[ny][nx]) - 65
            if visited[index] == False:
                visited[index] = True
                dfs(nx, ny, visited, cnt + 1)
                visited[index] = False
visited = [False for _ in range(26)]
visited[ord(alphaMap[0][0]) - 65] = True
dfs(0, 0, visited, 1)
print(rslt)

    
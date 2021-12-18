# [Gold 4] 치즈
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
paper = []
step = -1
check = False
startNode = [(0, 0), (0, m -1), (n - 1, 0), (n - 1, m - 1)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(start):
    chck = False
    queue = deque([start])
    paper[start[0]][start[1]] = -1
    while queue:
        y, x = queue.popleft() 
        for i in range(4):
            if 0 <= y + dy[i] < n and 0 <= x + dx[i] < m: 
                if paper[y + dy[i]][x + dx[i]] >= 1:
                        paper[y + dy[i]][x + dx[i]] += 1 
                elif paper[y + dy[i]][x + dx[i]] == 0:
                    paper[y + dy[i]][x + dx[i]] = -1 
                    queue.append((y + dy[i], x + dx[i]))

for y in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))
cnt = 0
while check == False:
    check = True
    for i in range(4):
        dfs(startNode[i]) 
    for y in range(n):
        for x in range(m):
            if paper[y][x] >= 3 :
                paper[y][x] = 0 
                check = False
            if paper[y][x] >= 1:
                paper[y][x] = 1
                check = False
            elif paper[y][x] < 0:
                paper[y][x] = 0
    cnt += 1

print(cnt - 1)
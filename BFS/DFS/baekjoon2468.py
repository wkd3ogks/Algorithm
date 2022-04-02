# [Silver 1] 안전 영역
# 1. 물에 잠기는 부분을 1로 설정한다.(잠기지 않은 부분은 0)
# 2. 만약 물이 잠기지 않은 부분에 대해서 움직인다.(물에 잠긴것으로 설정)
# 3. 처음 체크할 때 물에 잠기지 않았다면 그 것을 카운트한다.
from collections import deque

n = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
    
def solve(floodHeight):
    floodMap = [[0 for _ in range(n)]for _ in range(n)]
    startNode = []
    rslt = 0
    for y in range(n):
        for x in range(n):
            if board[y][x] <= floodHeight:
                floodMap[y][x] = 1
            else:
                startNode.append((y, x))
    while startNode:
        startY, startX = startNode.pop()
        queue = deque([(startY, startX)])
        if floodMap[startY][startX] == 0:
            rslt += 1
            floodMap[startY][startX] = 1
            while queue:
                y, x = queue.popleft()
                for i in range(4):
                    if 0 <= y + dy[i] < n and 0 <= x + dx[i] < n:
                        if floodMap[y + dy[i]][x + dx[i]] != 1:
                            floodMap[y + dy[i]][x + dx[i]] = 1
                            queue.append((y + dy[i], x + dx[i]))
    return rslt
max = -1
for height in range(0, 101):
    tempResult = solve(height)
    if max < tempResult:
        max = tempResult
print(max)

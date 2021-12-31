# [Gold 2] 2048(EASy)
import copy
from collections import deque
n = int(input())
board = []
result = 0
for y in range(n):
    board.append(list(map(int, input().split())))
    for x in range(n):
        if result < board[y][x]:
            result = board[y][x]

queue = deque([((board, result), 0)])

def up(board):
    upMax = -1
    changed = set()
    board2 = copy.deepcopy(board)
    for y in range(1, n):
        for x in range(n):
            ny = y
            if board2[y][x] != 0:
                # 빈칸이 없도록 끝까지 움직이기
                while ny > 0 and board2[ny - 1][x] == 0:
                    board2[ny - 1][x] = board2[ny][x]
                    board2[ny][x] = 0 
                    ny -= 1
                check = str(x) + str(ny)
                if ny != 0 and board2[ny - 1][x] == board2[ny][x] and not check in changed:
                    board2[ny - 1][x] = board2[ny][x] * 2
                    changed.add(check)
                    if upMax < board2[ny - 1][x]:
                        upMax = board2[ny - 1][x]
                    board2[ny][x] = 0
    return board2, upMax

def down(board):            
    downMax = -1
    changed = set()
    board2 = copy.deepcopy(board)
    for y in range(n - 2, -1, -1):
        for x in range(n):
            ny = y
            if board2[y][x] != 0:
                # 빈칸이 없도록 끝까지 움직이기
                while ny < n - 1 and board2[ny + 1][x] == 0 :
                    board2[ny + 1][x] = board2[ny][x]
                    board2[ny][x] = 0 
                    ny += 1
                check = str(x) + str(ny)
                if ny != n - 1 and board2[ny + 1][x] == board2[ny][x] and not check in changed:
                    board2[ny + 1][x] = board2[ny][x] * 2
                    changed.add(check)
                    if downMax < board2[ny + 1][x]:
                        downMax = board2[ny + 1][x]
                    board2[ny][x] = 0
    return board2, downMax

def left(board):            
    leftMax = -1
    changed = set()
    board2 = copy.deepcopy(board)
    for y in range(n):
        for x in range(1, n):
            nx = x
            if board2[y][x] != 0:
                # 빈칸이 없도록 끝까지 움직이기
                while nx > 0 and board2[y][nx - 1] == 0:
                    board2[y][nx - 1] = board2[y][nx]
                    board2[y][nx] = 0 
                    nx -= 1
                check = str(nx) + str(y)
                if nx != 0 and board2[y][nx - 1] == board2[y][nx] and not check in changed:
                    board2[y][nx - 1] = board2[y][nx] * 2
                    changed.add(check)
                    if leftMax < board2[y][nx - 1]:
                        leftMax = board2[y][nx - 1]
                    board2[y][nx] = 0
    return board2, leftMax

def right(board):            
    rightMax = -1
    changed = set()
    board2 = copy.deepcopy(board)
    for y in range(n):
        for x in range(n - 2, -1, -1):
            nx = x
            if board2[y][x] != 0:
                # 빈칸이 없도록 끝까지 움직이기
                while nx < n - 1 and board2[y][nx + 1] == 0 :
                    board2[y][nx + 1] = board2[y][nx]
                    board2[y][nx] = 0 
                    nx += 1
                check = str(nx) + str(y)
                if nx != n - 1 and board2[y][nx + 1] == board2[y][nx] and not check in changed:
                    board2[y][nx + 1] = board2[y][nx] * 2
                    changed.add(check)
                    if rightMax < board2[y][nx + 1]:
                        rightMax = board2[y][nx + 1]
                    board2[y][nx] = 0
    return board2, rightMax
def solve(result):
    rslt = result
    while queue:
        newBoard, cnt = queue.popleft()
        if cnt > 5:
            continue
        rslt = max(newBoard[1], rslt)
        queue.append((right(newBoard[0]), cnt + 1))
        queue.append((left(newBoard[0]), cnt + 1))
        queue.append((down(newBoard[0]), cnt + 1))
        queue.append((up(newBoard[0]), cnt + 1))
    for i in range(n):
        print(board[i])
    return rslt 

#print(left(board))
print(solve(result))
       
        



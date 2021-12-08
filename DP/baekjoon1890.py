# [Silver 2] 점프
import sys
n = int(input())
board = []
memo = []
for y in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
    memo.append([0 for _ in range(n)])
memo[0][0] = 1

for y in range(n):
    for x in range(n):
        if x < x + board[y][x] < n:
            memo[y][x + board[y][x]] += memo[y][x]
        if y < y + board[y][x] < n:
            memo[y + board[y][x]][x] += memo[y][x]
print(memo[n-1][n-1])


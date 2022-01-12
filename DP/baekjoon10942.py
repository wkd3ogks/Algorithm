# [Gold 3] 팰린드롬?
import sys

input = sys.stdin.readline
n = int(input())
seq = list(map(int, input().split()))
m = int(input())
memo = [[0 for _ in range(n)] for __ in range(n)]

# 1개 팰린드롬
for i in range(n):
    memo[i][i] = 1

# 2개 팰린드롬
for i in range(n - 1):
    if seq[i] == seq[i + 1]:
        memo[i][i + 1] = 1

# 3개부터 그 이상(와....)
for x in range(2, n):
    for i in range(n - x):
        j = i + x
        if memo[i + 1][j - 1] == 1 and seq[i] == seq[j]:
            memo[i][j] = 1

for _ in range(m):
    a, b = map(int, input().split())
    print(memo[a - 1][b - 1])



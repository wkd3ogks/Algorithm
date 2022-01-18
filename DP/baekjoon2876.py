# [Silver 2] 그래픽스 퀴즈
import sys
input = sys.stdin.readline

n = int(input())
max = -1
grade = -1
dp = [[0 for _ in range(6)] for _ in range(n + 1)]
for i in range(1, n + 1):
    a, b = map(int, input().split())
    dp[i][a] = dp[i - 1][a] + 1
    dp[i][b] = dp[i - 1][b] + 1
    if a < b:
        if dp[i][a] > max:
            max = dp[i][a]
            grade = a
        if dp[i][b] > max:
            max = dp[i][b]
            grade = b
    else:
        if dp[i][b] > max:
            max = dp[i][b]
            grade = b
        if dp[i][a] > max:
            max = dp[i][a]
            grade = a
print(max, grade)


# [Gold 3] 행렬 곱셈 순서
# 이 문제는 마치 Baekjoon10942 문제같다..
# 항상 최소값으로 대체 왜냐? 결과로 나오는 r, c는 항상 같기 때문이다!
import sys
input = sys.stdin.readline

def product(a, b, c, d):
    return (a, d, a * b * d)

n = int(input())
memo = [[[-1, -1, -1] for _ in range(n)] for __ in range(n)]

for i in range(n):
    r, c = map(int, input().split())
    memo[i][i] = [r, c, 0]
for i in range(n - 1):
    memo[i][i + 1] = [memo[i][i][0], memo[i + 1][i + 1][1], memo[i][i][0] * memo[i][i][1] * memo[i + 1][i + 1][1]]
    memo[i + 1][i] = [memo[i][i][0], memo[i + 1][i + 1][1], memo[i][i][0] * memo[i][i][1] * memo[i + 1][i + 1][1]]
print(memo)
for x in range(2, n):
    for i in range(n - x):
        j = i + x
        memo[j][i]


# [Gold 3] 팰린드롬?
# 1. 모든 경우를 탐색하려면 최악의 경우에 1,000,000 * 2,000 으로 불가능
# 2. 그럼 정보를 효율적으로 저장해야하는데 어떻게 저장할까?
# 3. 가능 케이스를 분류하자.
# 3 - 1. 1 2 1 3 1 2 1  - 2. 1 2 3 2 1
# 팰린드롬 수 안에 팰린드롬 수가 있다. -> 2 3 2, 1 2 3 2 1
# 정보를 어떻게 저장할까?
import sys
import time

n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
memo = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    left, right = 0, 0
    check1, check2, check3 = True, True, True
    while check1 or check2 or check3:
        if check1 and i + right < n and i - left >= 0:
            if check1 and seq[i - left] == seq[i + right]:
                # memo[i + right][i - left] = 1
                memo[i - left][i + right] = 1
            else:
                check1 = False
        else:
            check1 = False
        if check2 and i - left >= 0:
            if seq[i - left] == seq[i]:
                memo[i][i - left] = 1
                # memo[i - left][i] = 1
            else:
                check2 = False
        else:
            check2 = False
        if check3 and i + right < n:
            if seq[i + right] == seq[i]:
                memo[i][i + right] = 1
                # memo[i + right][i] = 1
            else:
                check3 = False
        else:
            check3 = False
        left += 1
        right += 1
m = int(sys.stdin.readline())
for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(memo[s - 1][e - 1])


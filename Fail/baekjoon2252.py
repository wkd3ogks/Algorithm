# [Gold 3] 줄 세우기
# 전체탐색으론 안될것 같고 그럼 결국 버려지는 정보가 없도록 해야하는데 어떻게?
import sys
n, m = map(int, sys.stdin.readline().split())
memo = [1 for i in range(n + 1)]
memo2 = [[0, i] for i in range(n + 1)]
again = []
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split()) 
    memo[a] += 1
    again.append((a, b))
for a, b in again: 
    memo2[a][0] += memo[b]
memo2.sort(reverse=True)
for val, index in memo2:
    if index == 0:
        continue
    print(index, end=' ')
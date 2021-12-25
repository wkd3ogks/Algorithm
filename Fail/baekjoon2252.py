# [Gold 3] 줄 세우기
# 전체탐색으론 안될것 같고 그럼 결국 버려지는 정보가 없도록 해야하는데 어떻게?
# 앞사람 수 말고 뒷사람 수를 저장하면?
import sys
n, m = map(int, sys.stdin.readline().split())
memo = [0 for i in range(n + 1)]
again = []
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split()) 
    if memo[a] < memo[b] + 1:
        memo[a] = memo[b] + 1
print(memo)
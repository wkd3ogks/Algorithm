# [Gold 3] 팰린드롬?
# 1. 모든 경우를 탐색하려면 최악의 경우에 1,000,000 * 2,000 으로 불가능
# 2. 그럼 정보를 효율적으로 저장해야하는데 어떻게 저장할까?
# 3. 가능 케이스를 분류하자.
# 3 - 1. 1 2 1 3 1 2 1  - 2. 1 2 3 2 1
# 팰린드롬 수 안에 팰린드롬 수가 있다. -> 2 3 2, 1 2 3 2 1
# 정보를 어떻게 저장할까?
import sys

input = sys.stdin.readline
n = int(input())
seq = list(map(int, input().split()))
m = int(input())
memo = [[0 for _ in range(n)] for __ in range(n)]
print(memo)
for i in range(n):
    check = [seq[i]] 
    for j in range(i, n):
        if j - i == 0:
            pass
        elif (j - i) % 2 == 0:
            pass
        else:
            pass

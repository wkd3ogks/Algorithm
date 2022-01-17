# [Gold 5] 동전 1
# "사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다."
# 무조건 큰 수만 더할 수 있도록 조건을 추가하면 해결된다.

n, k = map(int, input().split())
memo = [[0 for _ in range(n)] for _ in range(k + 1)]
coins = [0]
for i in range(n):
    h = int(input())
    coins.append(h)
    memo[h][i] += 1
print(memo)
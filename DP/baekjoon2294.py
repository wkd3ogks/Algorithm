# [Silver 2] 동전 2

n, k = map(int, input().split())
coins = set()
memo = [10001 for _ in range(k + 1)]
memo[0] = 0
for _ in range(n):
    coins.add(int(input()))

for goal in range(1, k + 1):
    for coin in coins:
        if goal - coin >= 0 and memo[goal] > memo[goal - coin] + 1:
            memo[goal] = memo[goal - coin] + 1

if memo[k] == 10001:
    print(-1)
else:
    print(memo[k])


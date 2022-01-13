# [Silver 1] 카드 구매하기

n = int(input())
cardPack = [0] + list(map(int, input().split()))
memo = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if memo[i - j] + cardPack[j] > memo[i]:
            memo[i] = memo[i - j] + cardPack[j]
print(memo[n])


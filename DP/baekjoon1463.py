# [Silver 3] 1로 만들기

n = int(input())
memo = [10**7 for _ in range(n + 1)]
memo[n] = 0

for i in range(n, 1, -1):
    if i % 3 == 0:
        if memo[i // 3] > memo[i] + 1:
            memo[i // 3] = memo[i] + 1
    if i % 2 == 0:
        if memo[i // 2] > memo[i] + 1:
            memo[i // 2] = memo[i] + 1
    if i - 1 >= 1:
        if memo[i - 1] > memo[i] + 1:
            memo[i - 1] = memo[i] + 1
print(memo[1])

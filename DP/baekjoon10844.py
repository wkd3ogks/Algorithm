# [Silver 1] 쉬운 계단 수

n = int(input())
memo = [1 for _ in range(10)]
dMemo = [0 for _ in range(10)]
memo[0] = 0
for _ in range(1, n):
    for i in range(0, 10):
        if i == 9:
            dMemo[i - 1] += memo[i]
            dMemo[i] -= memo[i]
        elif i == 0:
            dMemo[i + 1] += memo[i]
            dMemo[i] -= memo[i]
        else:
            dMemo[i + 1] += memo[i]
            dMemo[i - 1] += memo[i]
            dMemo[i] -= memo[i]
    for i in range(0, 10):
        memo[i] += dMemo[i]
        dMemo[i] = 0
total = 0
for i in range(10):
    total += memo[i]
print(total % 1000000000)
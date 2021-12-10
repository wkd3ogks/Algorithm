# [Gold 3] 가장 긴 바이토닉 부분 수열

n = int(input())
memo = [0 for _ in range(n)]
memo2 = [0 for _ in range(n)]
seq = list(map(int, input().split()))

#1000000
for i in range(n):
    memo[i] = 1
    for j in range(0, i):
        if seq[j] < seq[i]:
            if memo[i] < 1 + memo[j]:
                memo[i] = 1 + memo[j]
#1000000
for i in range(n - 1, -1, -1):
    memo2[i] = 1
    for j in range(n - 1, i, -1):
        if seq[j] < seq[i]:
            if memo2[i] < 1 + memo2[j]:
                memo2[i] = 1 + memo2[j]
max = 0
for i in range(n):
    if max < memo[i] + memo2[i] - 1:
        max = memo[i] + memo2[i] - 1
print(max)
# [Silver 2] 연속합
#Bottom Up 방식
n = int(input())
seq = list(map(int, input().split()))
max = -10000
memo = [0 for _ in range(n)]
for i in range(n):
    if i == 0:
        memo[0] = seq[i]
    else:
        if memo[i - 1] + seq[i] < seq[i]:
            memo[i] = seq[i]
        else:
            memo[i] = memo[i - 1] + seq[i]
    if memo[i] > max:
        max = memo[i]
print(max)


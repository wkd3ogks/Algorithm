# [Silver 2] 가장 큰 증가 부분 수열
n = int(input())
seq = [0] + list(map(int, input().split()))
dp = [0] + [seq[i] for i in range(1,n + 1)]
dp[0] = 0

for i in range(1, n + 1):
    temp = dp[i]
    for j in range(i - 1, 0, -1):
        if seq[i] >= seq[j] and dp[i] < temp + dp[j]:
            dp[i] = temp + dp[j]
print(max(dp))


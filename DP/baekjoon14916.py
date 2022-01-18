# [Silver 5] 거스름돈

n = int(input())
dp = [100000 for _ in range(100001)]
dp[2], dp[5] = 1, 1
for i in range(2, n + 1):
    if dp[i - 2] + 1 < dp[i]:
        dp[i] = dp[i - 2] + 1
    if i - 5 >= 0 and dp[i - 5] + 1 < dp[i]:
        dp[i] = dp[i - 5] + 1
if dp[n] == 100000:
    print(-1)
else:
    print(dp[n])


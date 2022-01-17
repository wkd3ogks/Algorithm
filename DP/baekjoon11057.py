# [Silver 1] 오르막길
n = int(input())

dp = [[0 for _ in range(10)] for _ in range(n + 1)]

for i in range(10):
    dp[1][i] = 1
# 100000
for k in range(2, n + 1):
    for i in range(10):
        for j in range(0, i + 1):
            dp[k][i] += dp[k - 1][j] 
total = 0
for i in dp[n]:
    total += i
print(total % 10007)


    

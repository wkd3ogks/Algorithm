# [Silver 1] 이항 계수2
import sys
sys.setrecursionlimit(2500)
n, k = map(int, input().split())
size = 0
if n > k:
    size = n
else:
    size = k
dp = [0 for _ in range(size + 1)]
def factorial(a):
    if dp[a] != 0:
        return dp[a]
    else:
        if a <= 1:
            dp[a] = 1
            return 1
        else:
            dp[a] = a * factorial(a - 1)
            return dp[a]
print((factorial(n) // (factorial(k) * factorial(n - k))) % 10007)
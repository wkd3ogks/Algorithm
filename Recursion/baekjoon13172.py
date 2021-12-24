# [Gold 5] Σ(Sigma)

import sys

# bX - 2 ≡ b-1 (mod X)
def bMinus1(b, x):
    if x == 1:
        return b
    else:
        if x % 2 == 0:
            return ((bMinus1(b, x // 2) % 1000000007) ** 2) % 1000000007
        else:
            return (((bMinus1(b, (x - 1) // 2) % 1000000007) ** 2) * (b % 1000000007)) % 1000000007

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b) 
def solve(a, b):
    temp = gcd(a, b)
    return ((a // temp) % 1000000007 * bMinus1((b // temp), 1000000005)) % 1000000007
n = int(sys.stdin.readline())
total = 0
for _ in range(n):
    b, a = map(int, sys.stdin.readline().split())
    total += solve(a, b)
print(total % 1000000007)
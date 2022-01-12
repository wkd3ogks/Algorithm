# [Blonze 1] 피보나치 수 2
import sys
input = sys.stdin.readline

n = int(input())
memo = [-1 for _ in range(n + 1)]
memo[0] = 0
memo[1] = 1

def Fibonacci(n):
    if memo[n] != -1:
        return memo[n]
    memo[n] = Fibonacci(n - 1) + Fibonacci(n - 2)
    return memo[n]
print(Fibonacci(n))
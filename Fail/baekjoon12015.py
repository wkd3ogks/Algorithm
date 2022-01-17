# [Gold 2] 가장 긴 증가하는 부분 수열 2
# 가장 크면서 가장 가까운 값


def upperBound(arr, find, right):
    left = 0
    mid = (left + right) // 2
    rslt = -1
    while left <= right:
        if arr[mid] > find:
            right = mid - 1
        elif arr[mid] > 

n = int(input())
seq = [0] + list(map(int, input().split()))
dp = [1 for _ in range(n + 1)]
arr = []
dp[0] = 0
for i in range(1, n + 1):
    arr.append(seq[i])
    arr.sort()
    

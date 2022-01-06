# [Gold 5] 용액

import sys
input = sys.stdin.readline

n = int(input())
liq = list(map(int, input().split()))
left = 0
right = n - 1
rslt = [-1, -1]
min = 3000000000
while left < right and right - 1 > -1 :
    if abs(liq[left] + liq[right]) < min:
        min = abs(liq[left] + liq[right])
        rslt[0] = liq[left]
        rslt[1] = liq[right]
    if left + 1 != right and abs(liq[left + 1] + liq[right]) < abs(liq[left] + liq[right - 1]):
        left += 1
    else:
        right -= 1
print(rslt[0], rslt[1])

# 양 끝 값은 각각 가능한 최대값 최소값. 
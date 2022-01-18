# [Gold 2] 가장 긴 증가하는 부분 수열 2
# 큰 값을 작은 값으로 바꿔도 항상 개수는 같다.
import sys
input = sys.stdin.readline
n = int(input())
seq = list(map(int, input().split()))
arr = []
length = 0
def Bound(arr, find, r):
    left = 0
    right = r
    mid = (left + right) // 2
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > find:
            right = mid
            if right == left:
                break
        elif arr[mid] < find:
            left = mid + 1
        else:
            return mid
    return mid
for i in range(n):
    if i == 0:
        arr.append(seq[i])
    elif arr[length] < seq[i]:
        arr.append(seq[i])
        length += 1
    elif arr[length] > seq[i]:
        arr[Bound(arr, seq[i], length)] = seq[i]
print(length + 1)


    

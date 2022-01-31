# [Silver 3] N과 M (1)
import sys

input = sys.stdin.readline
n, m = map(int , input().split())
arr = [i for i in range(n + 1)]
def recursion(arr, index, cnt, rslt):
    if cnt == m:
        print(*rslt)
        return
    for i in range(1, n + 1):
        if arr[i] != -1:
            arr[i] = -1
            rslt.append(i)
            recursion(arr, i, cnt + 1, rslt)
            rslt.pop()
            arr[i] = i
recursion(arr, 1, 0, [])


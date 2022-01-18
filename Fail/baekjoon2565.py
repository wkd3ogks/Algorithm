# [Gold 5] 전깃줄
import sys
connection = int(input())
dp = [[0 for _ in range(501)] for __ in range(501)]
arr = []
length = 0
for _ in range(connection):
    a, b = map(int, input().split())
    for start, end in arr:
        if start > a and b > end:
            dp[start][end] += 1
            dp[a][b] += 1
        elif start < a and b < end:
            dp[start][end] += 1
            dp[a][b] += 1
    arr.append((a, b))
    length += 1

check2 = [False for _ in range(length)]
def check():
    for start, end in arr:
        if dp[start][end] != 0:
            return True
    return False

def removeConnection():
    max1 = -1
    a, b = -1, -1 
    index = 0
    for i in range(length):
        if check2[i] == False:
            if dp[arr[i][0]][arr[i][1]] > max1:
                max1 = dp[arr[i][0]][arr[i][1]]
                a = arr[i][0]
                b = arr[i][1]
                index = i
    dp[a][b] = 0
    check2[index] = True
    return (a, b)

cnt = 0
while check():
    a, b = removeConnection()
    print("a, b",a, b, cnt)
    for i in range(length):
        if check2[i] == False:
            start, end = arr[i][0], arr[i][1]
            if start > a and b > end:
                dp[start][end] -= 1
                if dp[start][end] == 0:
                    check2[i] = True
            elif start < a and b < end:
                dp[start][end] -= 1
                if dp[start][end] == 0:
                    check2[i] = True
    cnt += 1
print(cnt)
        

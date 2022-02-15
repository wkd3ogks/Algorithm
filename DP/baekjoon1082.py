# [Gold 4] 방 번호
from copy import deepcopy
n = int(input())
p = list(map(int, input().split()))
m = int(input())
dp = [[] for _ in range(51)]
for number, cost in enumerate(p):
    if dp[cost]:
        if dp[cost][0] < number:
            dp[cost][0] = number
    else:
        dp[cost].append(number)

def lisToNumber(list1):
    if len(list1) > 0:
        list1.sort(reverse=True)
        number = ''
        for i in map(str, list1):
            number += i
    else:
        number = '0'
    return int(number)


for x in range(1, m + 1):
    for i, pi in enumerate(p):
        if x - pi >= 0 and dp[x - pi] != []:
            tmp = deepcopy(dp[x - pi])
            tmp.append(i)
            a, b = lisToNumber(tmp), lisToNumber(dp[x])
            if a >= b:
                dp[x] = tmp
max = 0
for i in range(m + 1):
    dp[i].sort(reverse=True)
    if len(dp[i]) > 0:
        a = int(''.join(map(str, dp[i])))
        if max < a:
            max = a
print(max)
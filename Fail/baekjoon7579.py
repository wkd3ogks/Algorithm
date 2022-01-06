# [Gold 3] 앱
# 앱을 선택할 때 팩토리얼을 선택하듯이.. M 이상이라면 바로 리턴
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(app, needTime, usedMemory):
    global minTime
    # print(app, needTime, usedMemory)
    if usedMemory >= m:
        if needTime < minTime:
            minTime = needTime
        return
    for nextApp in range(app + 1, n):
        dfs(nextApp, needTime + time[nextApp], usedMemory + memory[nextApp])

minTime = 100 * 100 + 1
n, m = map(int, input().split())
memory = list(map(int, input().split()))
time = list(map(int, input().split()))
for i in range(n):
    dfs(i, time[i], memory[i])
print(minTime)

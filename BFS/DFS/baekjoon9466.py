# [Gold 3] 텀 프로젝트
# 모든 문제든 단순하게! 생각하자!
import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline
def dfs(studnt, length):
    global rslt
    visited[studnt] = True
    cycle.append(studnt)
    if visited[students[studnt] - 1] == True:
        for i in range(length):
            if cycle[i] == students[studnt] - 1:
                for j in range(i, length):
                    rslt.append(cycle[j])
                return
        return
    return dfs(students[studnt] - 1, length + 1)

t = int(input())
for _ in range(t):
    n = int(input())
    total = 0
    students = list(map(int, input().split()))
    visited = [False for _ in range(n)]
    rslt = []
    for i in range(n):
        if visited[i] == False:
            cycle = []
            dfs(i, 1)
    print(n - len(rslt))


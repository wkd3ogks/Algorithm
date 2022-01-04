# [Gold 3] 텀 프로젝트
# Union-Find 문제
import sys
sys.setrecursionlimit(10**6)

def dfs(now, cnt, start):
    if students[now] == -1:
        return 0
    if start == students[now] - 1:
        return cnt 
    elif now == students[now] - 1:
        students[now] = -1
        return 1 
    else:
        if students[now] in studentList:
            studentList.remove(students[now])
        cnt += 1
        return dfs(students[now] - 1, cnt, start)
def solve():
    total = 0
    while studentList:
        student = studentList.pop() - 1
        total += dfs(student, 1, student)
    print(n - total)

t = int(input())
for _ in range(t):
    n = int(input())
    students = list(map(int, input().split()))
    studentList = set([i for i in range(n, 0, -1)])
    solve()
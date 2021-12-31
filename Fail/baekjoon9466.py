# [Gold 3] 텀 프로젝트

# 일반화
# 팀일 경우(처음 시작과 끝이 같을 때)
# 팀이면 값을 -1로 변경해두자
from typing import SupportsRound


def solve():
    n = int(input())
    students = list(map(int, input().split()))
    studentQueue = [i for i in range(n)]
    while studentQueue:
        check = studentQueue.pop(0)
        start = check
        tail = students[start] - 1
        team = set()
        while check != tail:
            if tail == -1:
                students[start] = 0
                studentQueue.remove(start)
                continue
            if start == tail:
                for i in team:
                    # -2 means not a Team 
                    students[i] = -2
                continue
            start = tail
            tail = students[tail] - 1
        for i in team:
            students[i] = 0 
        

        
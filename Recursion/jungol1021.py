# [Code : 1021] 장난감조립

n = int(input())
parts = [[] for _ in range(n + 1)]
rslt = [0 for _ in range(n + 1)]
m = int(input())

for _ in range(m):
    x, y, k = map(int, input().split())
    parts[x].append((y, k))

def findParts(part, cnt):
    global rslt
    if len(parts[part]) == 0:
        rslt[part] += cnt
    for needPart, needCnt in parts[part]:
        findParts(needPart, cnt * needCnt)

findParts(n, 1)

for i in range(1, n+1):
    if rslt[i] != 0:
        print(i, rslt[i])
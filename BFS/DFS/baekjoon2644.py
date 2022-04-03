# [Silver 2] 촌수 계산

n = int(input())

graph = [[]for _ in range(n + 1)]
first, last = map(int, input().split())

m = int(input())

for _ in range(m):
    parent, child = map(int, input().split())
    graph[child].append(parent)
    graph[parent].append(child)
rslt = -1
def findRelation(start, before, cnt):
    global rslt
    if start == last:
        rslt = cnt
        return
    for next in graph[start]:
        if next != before:
            findRelation(next, start, cnt + 1)

findRelation(first, -1, 0)
print(rslt)
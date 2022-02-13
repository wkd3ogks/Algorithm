# [Silver 1] 1로 만들기 2
# 당장에 집중하면 나머지는 반복문을 통해 해결가능하다.
from collections import deque
x = int(input())
visited = [[1000001, 1000001] for _ in range(x + 1)]
visited[x][0] = 0
queue = deque([x])
while queue:
    n = queue.popleft()
    if n % 3 == 0 and n // 3 >= 1:
        if visited[n // 3][0] > visited[n][0] + 1:
            visited[n // 3][0] = visited[n][0] + 1
            visited[n // 3][1] = n
            queue.append(n // 3)
    if n % 2 == 0 and n // 2 >= 1:
        if visited[n // 2][0] > visited[n][0] + 1:
            visited[n // 2][0] = visited[n][0] + 1
            visited[n // 2][1] = n
            queue.append(n // 2)
    if n - 1 >= 1:
        if visited[n - 1][0] > visited[n][0] + 1:
            visited[n - 1][0] = visited[n][0] + 1
            visited[n - 1][1] = n
            queue.append(n - 1)
rslt = []
queue = deque([1])
while queue:
    n = queue.popleft()
    rslt.append(n)
    if n != x:
        queue.append(visited[n][1])
print(visited[1][0])
while rslt:
    print(rslt.pop(), end=' ')
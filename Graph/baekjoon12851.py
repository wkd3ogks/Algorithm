# [Gold 5] 숨바꼭질 2
from collections import deque
visited = [0 for _ in range(200001)]
n, k = map(int, input().split())
visited[n] = 1
cnt = 0
def solve():
    global cnt
    queue = deque([n])
    while queue:
        node = queue.popleft()
        if 0 <= 2 * node <= 200000:
            if visited[2 * node] == 0 or visited[2 * node] >= visited[node] + 1:
                queue.append(2 * node)
                visited[2 * node] = visited[node] + 1
                if 2 * node == k and visited[2 * node] > visited[node] + 1:
                    cnt = 1
                elif 2 * node == k:
                    cnt += 1

        if 0 <= node + 1 <= 200000:
            if visited[node + 1] == 0 or visited[node + 1] >= visited[node] + 1:
                queue.append(node + 1)
                visited[node + 1] = visited[node] + 1
                if node + 1 == k and visited[node + 1] > visited[node] + 1:
                    cnt = 1
                elif node + 1 == k:
                    cnt += 1
        if 0 <= node - 1 <= 200000:
            if visited[node - 1] == 0 or visited[node - 1] >= visited[node] + 1:
                queue.append(node - 1)
                visited[node - 1] = visited[node] + 1
                if node - 1 == k and visited[node - 1] > visited[node] - 1:
                    cnt = 1
                elif node - 1 == k:
                    cnt += 1
solve()
print(visited[k] - 1)
if n == k:
    print(1)
else:
    print(cnt)
# [Gold 5] 파이프 옮기기
import sys
n = int(sys.stdin.readline())
grid= []
dx = [1, 0, 1]
dy = [0, 1, 1]
for _ in range(n):
    grid.append(sys.stdin.readline().rstrip().split())
queue = [(1, 0, 'width')]
result = 0
if grid[n-1][n - 1] != 1:
    while queue:
        x, y, method = queue.pop()
        if x == n - 1 and y == n - 1:
            result += 1
        cnt = 0
        if method == 'width':
            if 0 <= x + 1 < n:
                if grid[y][x + 1] == '0':
                    queue.append((x + 1, y, 'width'))
            if 0 <= x + 1 < n and 0 <= y + 1 < n:
                if grid[y][x + 1] == '0' and grid[y + 1][x] == '0' and grid[y + 1][x + 1] == '0':
                    queue.append((x + 1, y + 1, 'cross')) 
        elif method == 'height':
            if 0 <= y + 1 < n:
                if grid[y + 1][x] == '0':
                    queue.append((x, y + 1, 'height'))
            if 0 <= x + 1 < n and 0 <= y + 1 < n:
                if grid[y][x + 1] == '0' and grid[y + 1][x] == '0' and grid[y + 1][x + 1] == '0':
                    queue.append((x + 1, y + 1, 'cross')) 
        else:
            if 0 <= x + 1 < n:
                if grid[y][x + 1] == '0':
                    queue.append((x + 1, y, 'width'))
            if 0 <= y + 1 < n:
                if grid[y + 1][x] == '0':
                    queue.append((x, y + 1, 'height'))
            if 0 <= x + 1 < n and 0 <= y + 1 < n:
                if grid[y][x + 1] == '0' and grid[y + 1][x] == '0' and grid[y + 1][x + 1] == '0':
                    queue.append((x + 1, y + 1, 'cross')) 


            
print(result)


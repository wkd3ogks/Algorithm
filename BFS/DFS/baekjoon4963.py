delta = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,-1),(-1,1)]

def solve(queue, board, visited):
    cnt = 0
    for start in queue:
        print("Hi", start)
        realq = [start]
        if visited[start[1]][start[0]] == False:
            cnt += 1
            visited[start[1]][start[0]] = True
            while realq:
                x, y = realq.pop()
                for dx, dy in delta:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < w and 0 <= ny < h and board[ny][nx] == 1:
                        if visited[ny][nx] == False:
                            visited[ny][nx] = True
                            realq.append((nx, ny))
    print(cnt)

w, h = map(int, input().split())
while w != 0 and h != 0:
    visited = [[False for _ in range(w)] for __ in range(h)]
    print(visited)
    board = []
    queue = []
    for y in range(h):
        board.append(list(map(int, input().split())))
        for x in range(w):
            if board[y][x] == 1:
                queue.append((x, y))
    solve(queue, board, visited)
    w, h = map(int, input().split())
    
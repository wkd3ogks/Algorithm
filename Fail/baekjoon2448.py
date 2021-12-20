import sys
n = int(sys.stdin.readline())
realMap = [[ ' ' for __ in range(2 * n)] for _ in range(n)]
triangle = [
    [' ', ' ', '*', ' ',' ', ' '],
    [' ', '*', ' ', '*',' ', ' '],
    ['*', '*', '*', '*', '*', ' ']
]
def solve(height, width, y, x):
    if height == 3 and width == 6:
        for i in range(y, y + 3):
            for j in range(x, x + 6):
                realMap[i][j] = triangle[i - y][j - x]
    else:
        solve(height // 2, width // 2, y, x + height // 2)
        solve(height // 2, width // 2, y + height // 2, x)
        solve(height // 2, width // 2, y + height // 2, x + height)
    
solve(n, 2 * n, 0, 0)
for y in range(n):
    string = ''
    for x in range(2 * n):
        string += realMap[y][x]
    print(string)

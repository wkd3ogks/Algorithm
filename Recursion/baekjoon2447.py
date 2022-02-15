# [Silver 1] 별 찍기 - 10
pattern = [['*', '*', '*'],['*', ' ', '*'],['*', '*', '*']]
n = int(input())
paper = [[' ' for i in range(n)] for _ in range(n)] 

def solve(x, y, n):
    if n == 3:
        for i in range(y, y + 3):
            for j in range(x, x + 3):
                paper[i][j] = pattern[i - y][j - x]
    else:
        solve(x, y, n // 3)
        solve(x + n // 3, y, n // 3)
        solve(x + (n // 3) * 2, y, n//3)
        solve(x, y + n // 3, n // 3)
        solve(x + (n // 3) * 2, y + n // 3, n // 3)
        solve(x, y + (n // 3) * 2, n // 3)
        solve(x + n // 3, y + (n // 3) * 2, n // 3)
        solve(x + (n // 3) * 2, y + (n // 3) * 2, n // 3)
solve(0, 0, n)
for i in paper:
    print(''.join(i))
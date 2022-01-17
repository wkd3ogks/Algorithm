# [Silver 2] 신나는 함수 실행
a, b, c = map(int, input().split())
memo = [[[-1] * (c + 1)] * (b + 1)] * (a + 1)
def w(a, b, c):
    if memo[a][b][c] != 1:
        return memo[a][b][c]
    else:
        if a <= 0 or b <= 0 or c <= 0:
            memo[a][b][c] = 1
            return 1
    
        if a > 20 or b > 20 or c > 20:
            tmp = w(20, 20, 20)
            memo[a][b][c] = tmp
            return memo[20][20][20]

        if a < b and b < c:
            add1, add2, add3 = 0, 0, 0
            if memo[a][b][c - 1] != -1:
                add1 = memo[a][b][c - 1]
            else:
                add1 = w(a, b, c - 1)
            if memo[a][b - 1][c - 1] != -1:
                add2 = memo[a][b - 1][c - 1]
            else:
                add2 = w(a, b - 1, c - 1)
            if memo[a][b - 1][c] != -1:
                add3 = memo[a][b - 1][c]
            else:
                add3 = w(a, b - 1, c)
            memo[a][b][c] = add1 + add2 - add3
            return add1 + add2 - add3

        add1, add2, add3, add4 = 0, 0, 0, 0
        if memo[a - 1][b][c] != -1:
            add1 = memo[a - 1][b][c]
        else:
            add1 = w(a - 1, b, c)
        if memo[a - 1][b - 1][c] != -1:
            add2 = memo[a - 1][b - 1][c]
        else:
            add2 = w(a - 1, b - 1, c)
        if memo[a - 1][b][c - 1] != -1:
            add3 = memo[a - 1][b][c - 1]
        else:
            add3 = w(a - 1, b, c - 1)
        if memo[a - 1][b - 1][c - 1] != -1:
            add4 = memo[a - 1][b - 1][c - 1]
        else:
            add4 = w(a - 1, b - 1, c - 1)
        memo[a][b][c] = add1 + add2 + add3 - add4
        return add1 + add2 + add3 - add4
print(w(a, b, c))

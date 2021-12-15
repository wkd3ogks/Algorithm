# [Gold 4] 행렬 제곱
matrix = []
n, b = map(int, input().split())
for i in range(n):
    matrix.append(list(map(int, input().split())))

def multi(matrix1, matrix2):
    value = []
    for y in range(n):
        value.append([])
        for x in range(n):
            tmp = 0
            for i in range(n):
                tmp += matrix1[y][i] * matrix2[i][x]
            value[y].append(tmp % 1000)
    return value
def solve(b):
    if b <= 1:
        return matrix
    if b % 2 == 0:
        tmp = solve(b // 2)
        return multi(tmp, tmp)  
    else:
        tmp = solve((b - 1) // 2)
        return multi(multi(tmp, tmp), matrix)

for row in solve(b):
    for col in row:
        # col % 1000해주는 이유는 첫 Matrix를 %1000 안해서 생기는 문제를 해결하기 위해서..
        print(col % 1000, end=' ')
    print()



# [Gold 3] 피보나치 수 6
# [+] 모듈러 연산 분배법칙
# (A + B) % p = ((A % p) + (B % p)) % p
# (A * B) % p = ((A % p) * (B % p)) % p
# (A - B) % p = ((A % p) - (B % p) + p) % p

n = int(input())
matrix = [[1, 1],[1, 0]]
def matrixProduct(matrix1, matrix2):
    return [[(matrix1[0][0] * matrix2[0][0] + matrix1[0][1] * matrix2[1][0]) % 1000000007, (matrix1[0][0] * matrix2[0][1] + matrix1[0][1] * matrix2[1][1]) % 1000000007],
    [(matrix1[1][0] * matrix2[0][0] + matrix1[1][1] * matrix2[1][0]) % 1000000007, (matrix1[1][0] * matrix2[0][1] + matrix1[1][1] * matrix2[1][1]) % 1000000007]]
def fibonacci3(n):
    if n <= 1:
        return matrix
    else:
        if n % 2 == 0:
            temp = fibonacci3(n // 2)
            return matrixProduct(temp, temp) 
        else:
            temp = fibonacci3((n - 1) // 2)
            return matrixProduct(matrixProduct(temp, temp), matrix)
print(fibonacci3(n)[0][1] )
# 1. Recursion
# Time Complexity : O(2^n)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10)) # 55

# 2. Loop
# Time Complexity : O(n)
def fibonacci2(n):
    i = 2
    left, right = 0, 1
    while i <= n:
        left, right = right, left + right
        i += 1
    return right
print(fibonacci2(10))

# 3. Dynamic Programming

# 4. Matrix
matrix = [[1, 1],[1, 0]]
def matrixProduct(matrix1, matrix2):
    return [[matrix1[0][0] * matrix2[0][0] + matrix1[0][1] * matrix2[1][0], matrix1[0][0] * matrix2[0][1] + matrix1[0][1] * matrix2[1][1]],
    [matrix1[1][0] * matrix2[0][0] + matrix1[1][1] * matrix2[1][0], matrix1[1][0] * matrix2[0][1] + matrix1[1][1] * matrix2[1][1]]]
def fibonacci3(n):
    if n <= 1:
        return matrix
    else:
        if n % 2 == 0:
            temp = fibonacci3(n // 2)
            return matrixProduct(temp, temp) 
        else:
            temp = fibonacci3(n // 2)
            return matrixProduct(matrixProduct(temp, temp), matrix)
print(fibonacci3(3)[0][1])


# 5. General Term


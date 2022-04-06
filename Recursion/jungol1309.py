# [Code 1309] 팩토리얼
def factorial(n, rslt):
    if n == 1:
        print("1! = 1")
        return rslt 
    print("%d! = %d * %d!" % (n, n, n - 1))
    return factorial(n - 1, rslt * n) 
print(factorial(int(input()), 1))

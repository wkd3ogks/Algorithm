# [Gold 5] 감소하는 수
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9]
n = int(input())
cnt = 0 
def solve(num, rslt):
    global cnt
    if cnt == n:
        print(rslt)
        return rslt
    for i in arr:
        if i < num:
            cnt += 1
            solve(i, rslt + str(i))
for i in range(10):
    solve(i, str(i))
        

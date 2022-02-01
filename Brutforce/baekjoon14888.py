# [Silver 1] 연산자 끼워넣기
from lib2to3.pgen2.grammar import opmap_raw


n = int(input())
seq = list(map(int, input().split()))[::-1]
operator = list(map(int, input().split())) # + - * //
ans1 = -100000000000
ans2 = 100000000000
def solve(seq, operator, rslt):
    global ans1, ans2
    if sum(operator) == 0:
        if ans1 < rslt:
            ans1 = rslt
        if ans2 > rslt:
            ans2 = rslt
        return
    for i in range(4):
        if operator[i] != 0:
            a = seq.pop()
            before = rslt
            operator[i] -= 1
            if i == 0:
                rslt += a
                solve(seq, operator, rslt)
                rslt = before
            elif i == 1:
                rslt -= a
                solve(seq, operator, rslt)
                rslt = before
            elif i == 2:
                rslt *= a
                solve(seq, operator, rslt)
                rslt = before
            else:
                if rslt < 0:
                    rslt = -(abs(rslt) // a)
                else:
                    rslt //= a
                solve(seq, operator, rslt)
                rslt = before
            seq.append(a)
            operator[i] += 1
solve(seq,operator, seq.pop())            
print(ans1)
print(ans2)



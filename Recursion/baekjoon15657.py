import sys
n, m = map(int, sys.stdin.readline().split())
seq = list(map(int, sys.stdin.readline().rstrip().split()))
seq.sort()

def solve(seq, rslt, cnt, n):
    if cnt == m:
        for i in rslt:
            print(i, end=' ') 
        print()
        return
    for i in range(n):
        rslt.append(seq[i])
        cnt += 1
        solve(seq[i:n], rslt, cnt, n - i)
        rslt.pop()
        cnt -= 1

solve(seq, [], 0, n)   


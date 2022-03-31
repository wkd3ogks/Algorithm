n, m = map(int, input().split())

def solve(cnt, rslt):
    if cnt == m:
        for j in rslt:
            print(j, end=' ')
        print()
        return
    for i in range(1, n + 1):
        rslt.append(i)
        solve(cnt + 1, rslt)
        rslt.pop()

solve(0, [])

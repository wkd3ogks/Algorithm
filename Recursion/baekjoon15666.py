# [Silver 2] N과 M(12)
n, m = map(int, input().split())
temp = map(int, input().split())
seq = set()
for i in temp:
    seq.add(i)
seq = list(seq)
seq.sort()

def solve(seq, rslt, cnt):
    if cnt == m:
        for i in rslt:
            print(i, end=' ')
        print()
        return
    for i in range(len(seq)):
        rslt.append(seq[i])
        cnt += 1
        solve(seq[i:], rslt, cnt)
        cnt -= 1
        rslt.pop()
        
solve(seq, [], 0)
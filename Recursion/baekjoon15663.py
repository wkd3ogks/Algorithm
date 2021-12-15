# [Silver 2] N과 M(9)
n, m = map(int, input().split())
seq = list(map(int, input().split()))
result = [] 

seq.sort()
def solve(seq, rslt, cnt):
    global result
    if cnt == m:
        result.append(rslt)
        return
    for i in range(len(seq)):
        original = rslt
        rslt += str(seq[i]) + " "
        cnt += 1
        solve(seq[:i] + seq[i + 1:], rslt, cnt)
        cnt -= 1
        rslt = original
solve(seq, "", 0)
check = set()
for i in result:
    if not i in check:
        print(i)
        check.add(i)
        

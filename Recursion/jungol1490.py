# [Code 1490] next Combination

n, k = map(int, input().split())
quest = list(map(int, input().split()))
ans = []
def Combination(num, cnt, rslt):
    if cnt == k:
        data = []
        for i in rslt:
            data.append(i)
        ans.append(data)
    if num >= n + 1:
        return
    for i in range(num, n + 1):
        rslt.append(i)
        Combination(i + 1, cnt + 1, rslt)
        rslt.pop()
Combination(1, 0, [])
for i in range(len(ans)):
    if ans[i] == quest:
        if i + 1 < len(ans):
            for i in ans[i + 1]:
                print(i, end=' ')
            print()
        else:
            print("NONE")
        break
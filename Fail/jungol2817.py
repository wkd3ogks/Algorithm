# [Code 2817] : Lotto

arr = list(map(int, input().split()))

k = arr[0]
arr = arr[1:]

def lotto(now, cnt, rslt):
    if cnt == 6:
        for i in rslt:
            print(i, end=' ')
        print()
        return
    if now + 1 >= k:
        return
    for i in range(now, k):
        if rslt[-1] != arr[i]:
            rslt.append(lotto[now])
            lotto()

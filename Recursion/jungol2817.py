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
    if now >= k:
        return
    for i in range(now, k):
        rslt.append(arr[i])
        lotto(i + 1, cnt + 1, rslt)
        rslt.pop()
lotto(0, 0, [])

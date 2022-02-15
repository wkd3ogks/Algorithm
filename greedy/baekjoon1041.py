# [Gold 5] 주사위

n = int(input())
top, right, down, left, up, bottom = map(int, input().split())
if n > 1:
    min1 = min((top, right, down, left, up, bottom))
    min2 = min((left + up, left + down, right + up, right + down, top + left, top + right, top + up, top + down, bottom + left, bottom + right, bottom + up, bottom + down))
    min3 = min((top + left + up, top + left + down, top + right + up, top + right + down, bottom + left + up, bottom + left + down, bottom + right + up, bottom + right + down))
    print(min1, min2, min3)
    rslt = 0
    #TOP edge
    rslt += min3 * 4
    #TOP side 
    rslt += min2 * (n - 2) * 4
    #TOP middle
    rslt += ((n - 2) ** 2) * min1
    #Side edge
    rslt += 4 * min2
    #Side side
    rslt += (n - 2) * min2 * 4
    #Side Middle
    rslt += ((n - 2) ** 2) * min1 * 4
    #Side Down
    rslt += min1 * (n - 2) * 4
    print(rslt)
else:
    print(sum((top, right, down, left, up, bottom)) - max((top, right, down, left, up, bottom)))

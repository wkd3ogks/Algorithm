# [Silver 3] 선물

n, l, w, h = map(int, input().split())
min = l / n
if min > w / n:
    min = w / n
if min > h / n:
    min = h / n
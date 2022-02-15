#[Gold 4] RGB거리 2
# 푼 사람들의 글을 보면 시작점을 고정하는 방법을 이용한다.
RED = 0
GREEN = 1
BLUE = 2
INF = 1000 * 1000 + 1

houseCnt = int(input())
street = [None]

for _ in range(houseCnt):
    street.append(list(map(int, input().split())))


# minCost[houseCnt][StartColor][LastColor]
minCost = [[[INF, INF, INF], [INF, INF, INF], [INF, INF, INF]] for _ in range(houseCnt + 1)]
minCost[1][RED][RED], minCost[1][GREEN][GREEN], minCost[1][BLUE][BLUE] = street[1][RED], street[1][GREEN], street[1][BLUE]

for house in range(2, houseCnt + 1):
    minCost[house][RED][RED] = min(minCost[house - 1][RED][BLUE], minCost[house - 1][RED][GREEN]) + street[house][RED]
    minCost[house][GREEN][RED] = min(minCost[house - 1][GREEN][BLUE], minCost[house - 1][GREEN][GREEN]) + street[house][RED]
    minCost[house][BLUE][RED] = min(minCost[house - 1][BLUE][BLUE], minCost[house - 1][BLUE][GREEN]) + street[house][RED]

    minCost[house][RED][BLUE] = min(minCost[house - 1][RED][RED], minCost[house - 1][RED][GREEN]) + street[house][BLUE]
    minCost[house][GREEN][BLUE] = min(minCost[house - 1][GREEN][RED], minCost[house - 1][GREEN][GREEN]) + street[house][BLUE]
    minCost[house][BLUE][BLUE] = min(minCost[house - 1][BLUE][RED], minCost[house - 1][BLUE][GREEN]) + street[house][BLUE]

    minCost[house][RED][GREEN] = min(minCost[house - 1][RED][RED], minCost[house - 1][RED][BLUE]) + street[house][GREEN]
    minCost[house][BLUE][GREEN] = min(minCost[house - 1][BLUE][RED], minCost[house - 1][BLUE][BLUE]) + street[house][GREEN]
    minCost[house][GREEN][GREEN] = min(minCost[house - 1][GREEN][RED], minCost[house - 1][GREEN][BLUE]) + street[house][GREEN]
    
print(min(minCost[house][GREEN][RED], minCost[house][BLUE][RED], minCost[house][RED][BLUE], minCost[house][GREEN][BLUE], minCost[house][RED][GREEN], minCost[house][BLUE][GREEN]))
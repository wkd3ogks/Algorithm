# [Silver 1] 호텔

reqC, cityN = map(int, input().split())
marketing = []
for _ in range(cityN):
    marketing.append(list(map(int, input().split())))
memo = [1000000 for _ in range(reqC + 1)]
memo[0] = 0
for i in range(reqC + 1):
    for cost, clients in marketing:
        if i - clients <= 0:
            if memo[i] > cost:
                memo[i] = cost
        elif memo[i] > cost + memo[i - clients]:
                memo[i] = cost + memo[i - clients]
print(memo[reqC])
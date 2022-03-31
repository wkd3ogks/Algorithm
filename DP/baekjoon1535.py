# [Silver 2] 안녕

allPerson = int(input()) + 1

# lossHealth[PersonIndex], gainHappy[PersonIndex]
lossHealth = [0] + list(map(int, input().split()))
gainHappy = [0] + list(map(int, input().split()))


# maxHappy[SumLossHealth] = MaxHappy
maxHappy = [[0 for _ in range(100)] for __ in range(allPerson)]

for PersonIndex in range(allPerson):
    for sumLossHealth in range(100):
        if sumLossHealth >= lossHealth[PersonIndex]:
            maxHappy[PersonIndex][sumLossHealth] = max(maxHappy[PersonIndex - 1][sumLossHealth - lossHealth[PersonIndex]] + gainHappy[PersonIndex], maxHappy[PersonIndex - 1][sumLossHealth])
        else:
            maxHappy[PersonIndex][sumLossHealth] = maxHappy[PersonIndex - 1][sumLossHealth]
    
answer = -1
for y in range(allPerson):
    if answer < maxHappy[y][99]:
        answer = maxHappy[y][99]
print(answer)
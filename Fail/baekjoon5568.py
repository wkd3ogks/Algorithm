n = int(input())
k = int(input())
cards = []
resultSet = set()
for _ in range(n):
    cards.append(int(input()))

def chooseCard(index, cnt, rslt):
    global resultSet, cards
    if cnt == k:
        sum = ''
        for i in map(str, rslt):
            sum += i
        resultSet.add(int(sum))
    else:
        for i, num in enumerate(cards):
            rslt.append(num)
            cards.pop(i)
            print("num :",num)
            chooseCard(i + 1, cnt + 1, rslt)
            cards.append(num)
            rslt.pop()

chooseCard(0, 0, [])
print(resultSet)




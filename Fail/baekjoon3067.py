# [Gold 5] Coins

testCase = int(input())

def solve(n, coins, question):
    # possible[money] = Value
    possible = [[0 for _ in range(question + 1)] for __ in range(n + 1)]

    for money in range(question + 1):
        for coinIndex in range(1, n):
            coin = coins[coinIndex]
            if money >= coin:
                possible[coinIndex][money] = possible[coinIndex - 1][money - coin] + 1
            else:
                possible[coinIndex][money] = possible[coinIndex - 1][money]
    return possible[n - 1][question]

for _ in range(testCase):
    print(solve(int(input()) + 1, [0] + list(map(int, input().split())), int(input())))


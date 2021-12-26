# [Gold 5] LCS 2
# (Left), (Top), (Cross)

string1 = input()
string2 = input()
length1 = len(string1)
length2 = len(string2)

memo = [[[0, ''] for _ in range(length1 + 1)] for _ in range(length2 + 1)] 

for y in range(length2):
    for x in range(length1):
        if string2[y] == string1[x]:
            memo[y + 1][x + 1][0] = memo[y][x][0] + 1
            memo[y + 1][x + 1][1] = memo[y][x][1] + string1[x]
        else:
            left = memo[y + 1][x][0]
            top = memo[y][x + 1][0]
            if left < top:
                memo[y + 1][x + 1][0] = top 
                memo[y + 1][x + 1][1] = memo[y][x + 1][1]
            else:
                memo[y + 1][x + 1][0] = left
                memo[y + 1][x + 1][1] = memo[y + 1][x][1]
#for y in range(length2 + 1):
#    print(memo[y])
print(memo[length2][length1][0])
for i in memo[length2][length1][1]:
    print(i, end='')
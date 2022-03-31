# [Blonze 2] 일곱 난쟁이

from gettext import find


dwarfs = []

for _ in range(9):
    dwarfs.append(int(input()))

findAnswer = False

def solve(index, cnt, rslt):
    global findAnswer
    if findAnswer == True:
        return
    if cnt == 7:
        if sum(rslt) == 100:
            rslt.sort()
            print("\n".join(map(str, rslt)))
            findAnswer = True
        return
    for i in range(index, 9):
        rslt.append(dwarfs[i])
        solve(i + 1, cnt + 1, rslt)
        rslt.pop()

solve(0, 0, [])

    
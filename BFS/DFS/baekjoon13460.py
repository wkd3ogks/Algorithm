# [Gold 1] 구슬 탈출 2
# 첫 단추가 잘못 끼워졌네~ 그렇게 끝까지 모르는 체 다 채웠는데 다시 맞게 입으려면 다시 다 풀어야겠네 또.
from collections import deque

n, m = map(int, input().split())
# 가로 관련 데이터
wall1 = [[] for _ in range(n)]
length1 = [0 for _ in range(n)]
# 세로 관련 데이터
wall2 = [[] for _ in range(m)]
length2 = [0 for _ in range(m)]
data = []
rx, ry, bx, by, cnt = 0, 0, 0, 0, 0
goal = [0, 0] 
for y in range(n):
    data.append(input())
    for x in range(m):
        if data[y][x] == '#':
            wall1[y].append(x)
            length1[y] += 1
            wall2[x].append(y)
            length2[x] += 1
        elif data[y][x] == 'R':
            rx = x
            ry = y 
        elif data[y][x] == 'B':
            bx = x
            by = y
        elif data[y][x] == 'O':
            goal[0] = x
            goal[1] = y

print(goal)
result = -1
queue = deque([[rx, ry, bx, by, cnt]])
while queue:
    # print(queue)
    redX, redY, blueX, blueY, cnt = queue.popleft()
    # print(redX, redY, blueX, blueY, cnt)
    if cnt > 9:
        continue
    newRx, newRy, newBx, newBy = 0, 0, 0, 0
    cnt += 1
    check1 = False
    check2 = False
    isGoal = False
    # go right
    for i in range(10):
        if i < length1[redY] and wall1[redY][i] > redX and check1 == False:
            newRx = wall1[redY][i] - 1
            check1 = True
        if i < length1[blueY] and wall1[blueY][i] > blueX and check2 == False:
            newBx = wall1[blueY][i] - 1
            check2 = True
    if redX < goal[0] and newRx >= goal[0] and redY == goal[1]:
        if not (blueX < goal[0] and newBx >= goal[0] and blueY == goal[1]):
            result = cnt
            break
    elif blueX < goal[0] and newBx >= goal[0] and blueY == goal[1]:
        pass
    else:
        if newRx == newBx and redY == blueY:
            if redX > blueX:
                newBx -= 1
            else:
                newRx -= 1
        queue.append([newRx, redY, newBx, blueY, cnt])
    check1, check2 = False, False
    # print("Go Right :", newRx, redY, newBx, blueY, cnt)

    # go left
    for i in range(10):
        if i < length1[redY] and wall1[redY][i] < redX:
            newRx = wall1[redY][i] + 1
        if i < length1[blueY] and wall1[blueY][i] < blueX:
            newBx = wall1[blueY][i] + 1
    if redX > goal[0] and newRx <= goal[0] and redY == goal[1]:
        if not (blueX > goal[0] and newBx <= goal[0] and blueY == goal[1]):
            result = cnt
            break
    elif blueX > goal[0] and newBx <= goal[0] and blueY == goal[1]:
        pass
    else:
        if newRx == newBx and redY == blueY:
            if redX < blueX:
                newBx += 1 
            else:
                newRx += 1
        queue.append([newRx, redY, newBx, blueY, cnt])
    check1, check2 = False, False
    # print("Go Left :", newRx, redY, newBx, blueY, cnt)

    # go Bottom
    for i in range(10):
        if i < length2[redX] and wall2[redX][i] > redY and check1 == False:
            newRy = wall2[redX][i] - 1
            check1 = True
        if i < length2[blueX] and wall2[blueX][i] > blueY and check2 == False:
            newBy = wall2[blueX][i] - 1
            check2 = True
    if redY < goal[1] and newRy >= goal[1] and redX == goal[0]:
        if not (blueY < goal[1] and newBy >= goal[1] and blueX == goal[0]):
            result = cnt
            break
    elif blueY < goal[1] and newBy >= goal[1] and blueX == goal[0]:
        pass
    else:
        if newRy == newBy and redX == blueX:
            if redY > blueY:
                newBy -= 1 
            else:
                newRy -= 1
        queue.append([redX, newRy, blueX, newBy, cnt])
    check1, check2 = False, False
    # print("Go Bottom :", redX, newRy, blueX, newBy, cnt)

    # go Top
    for i in range(10):
        if i < length2[redX] and wall2[redX][i] < redY:
            newRy = wall2[redX][i] + 1
        if i < length2[blueX] and wall2[blueX][i] < blueY:
            newBy = wall2[blueX][i] + 1
    if redY > goal[1] and newRy <= goal[1] and redX == goal[0]:
        if not (blueY > goal[1] and newBy <= goal[1] and blueX == goal[0]):
            result = cnt
            break
    elif blueY > goal[1] and newBy <= goal[1] and blueX == goal[0]:
        pass
    else:
        if newRy == newBy and redX == blueX:
            if redY > blueY:
                newRy += 1 
            else:
                newBy += 1
        queue.append([redX, newRy, blueX, newBy, cnt])
    check1, check2 = False, False
    # print("Go Top :", redX, newRy, blueX, newBy, cnt)
print(result)


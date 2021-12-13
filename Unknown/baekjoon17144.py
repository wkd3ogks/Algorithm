import sys
r, c, t = map(int, sys.stdin.readline().split())
room = []
tempRoom = []
dusts = []
aircleaner = []
for k in range(r):
    room.append(list(map(int, sys.stdin.readline().split())))
    tempRoom.append([])
    for i in range(c):
        tempRoom[k].append(0)
        if room[k][i] == -1:
            aircleaner.append(k)

dy = [0, 0, 1, -1]             
dx = [1, -1, 0, 0]

def diffusion():
    dusts = []
    for y in range(r):
        for x in range(c):
            if room[y][x] > 0:
                dusts.append((y, x))
    change = set()
    for dustY, dustX in dusts:
        mainDust = room[dustY][dustX] 
        moveDust = mainDust // 5
        for i in range(4):
            if (0 <= dustX + dx[i] <= c - 1 and 0 <= dustY + dy[i] <= r - 1) and room[dustY + dy[i]][dustX + dx[i]] != -1:
                tempRoom[dustY + dy[i]][dustX + dx[i]] += moveDust
                change.add((dustY + dy[i], dustX + dx[i]))
                room[dustY][dustX] -= moveDust
    for dustY, dustX in change:
        room[dustY][dustX] = room[dustY][dustX] + tempRoom[dustY][dustX]
        tempRoom[dustY][dustX] = 0
def air():
    change = []
    locateX = 1
    locateY = aircleaner[0]
    while locateX <= c - 2:
        tempRoom[locateY][locateX + 1] = room[locateY][locateX] 
        change.append((locateY, locateX + 1))
        locateX += 1
    while locateY >= 1:
        tempRoom[locateY - 1][locateX] = room[locateY][locateX]
        change.append((locateY - 1, locateX))
        locateY -= 1
    while locateX >= 1:
        tempRoom[locateY][locateX - 1] = room[locateY][locateX] 
        change.append((locateY, locateX - 1))
        locateX -= 1
    while locateY <= aircleaner[0] - 1:
        tempRoom[locateY + 1][locateX] = room[locateY][locateX]
        change.append((locateY + 1, locateX))
        locateY += 1
    for y, x in change:
        room[y][x] = tempRoom[y][x]
        tempRoom[y][x] = 0
    tempRoom[aircleaner[0]][0] = -1
    room[aircleaner[0]][0] = -1
    room[aircleaner[0]][1] = 0

    change = []
    locateX = 1
    locateY = aircleaner[1]
    while locateX <= c - 2:
        tempRoom[locateY][locateX + 1] = room[locateY][locateX] 
        change.append((locateY, locateX + 1))
        locateX += 1
    while locateY <= r - 2:
        tempRoom[locateY + 1][locateX] = room[locateY][locateX]
        change.append((locateY + 1, locateX))
        locateY += 1
    while locateX >= 1:
        tempRoom[locateY][locateX - 1] = room[locateY][locateX] 
        change.append((locateY, locateX - 1))
        locateX -= 1
    while locateY >= aircleaner[1] + 1:
        tempRoom[locateY - 1][locateX] = room[locateY][locateX]
        change.append((locateY - 1, locateX))
        locateY -= 1
    for y, x in change:
        room[y][x] = tempRoom[y][x]
        tempRoom[y][x] = 0
    tempRoom[aircleaner[1]][0] = -1
    room[aircleaner[1]][0] = -1
    room[aircleaner[1]][1] = 0

for i in range(t):
    diffusion() 
    air()
cnt = 0
for y in room:
    for j in y:
        if j > 0:
            cnt += j
print(cnt)





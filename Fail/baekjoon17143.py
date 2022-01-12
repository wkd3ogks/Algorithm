# [Gold 2] 낚시왕
import sys
input = sys.stdin.readline

cnt = 0
fisher = -1
height, width, m = map(int, input().split())
sea = [[0 for _ in range(width)] for __ in range(height)]
sharks = dict()
for i in range(m):
    r, c, s, d, z = map(int, input().split())
    sharks[z] = [r - 1, c - 1, s, d, z]
    sea[r - 1][c - 1] = z
def printSea():
    for i in range(height):
        print(sea[i])

def moveFisher():
    global fisher
    fisher += 1

def catch():
    global cnt
    for i in range(height):
        if sea[i][fisher] != 0:
            del sharks[sea[i][fisher]]
            cnt += sea[i][fisher]
            sea[i][fisher] = 0
            return 1
    return 0 

def moveShark():
    for size in sharks:
        sea[sharks[size][0]][sharks[size][1]] = 0
        sharkY, sharkX, speed, direction, size = sharks[size]
        while speed > 0:
            if direction == 1:
                if sharkY - speed >= 0:
                    sharkY = sharkY - speed
                    break
                else:
                    direction = 2
                    speed = speed - sharkY
                    sharkY = 0
            if direction == 2:
                if sharkY + speed < height:
                    sharkY = sharkY +  speed
                    break
                else:
                    direction = 1
                    speed = sharkY + speed - (height - 1)
                    sharkY = height - 1
            if direction == 4:
                if sharkX - speed >= 0:
                    sharkX = sharkX - speed
                    break
                else:
                    direction = 3
                    speed = abs(sharkX - speed)
                    sharkX = 0
            if direction == 3:
                if sharkX + speed < width:
                    sharkX = sharkX + speed
                    break
                else:
                    direction = 4
                    speed = sharkX + speed - (width - 1)
                    sharkX = width - 1
        sharks[size][0] = sharkY
        sharks[size][1] = sharkX
        sharks[size][3] = direction
    removeItems = []
    for size in sharks:
        sharkY, sharkX, speed, direction, size = sharks[size]
        if sea[sharkY][sharkX] < sharks[size][4]:
            if sea[sharkY][sharkX] != 0:
                removeItems.append(sea[sharkY][sharkX])
            sea[sharkY][sharkX] = size
        else:
            removeItems.append(size)
    for i in removeItems:
        del sharks[i]

def Onesec():
    catch()
    moveShark()

while fisher < width - 1:
    fisher += 1
    Onesec()
print(cnt)

# [Blonze 2] 24

def timeToSec():
    timeArr = list(map(int, input().split(':')))
    return timeArr[0] * 60 ** 2 + timeArr[1] * 60 + timeArr[2]

def secToTime():
    pass


nowTime = timeToSec()

startTime = timeToSec()

time = 0
rslt = ["00", "00", "00"]
if nowTime < startTime:
    time = (24 * 60 * 60 - startTime) + nowTime
else:
    time = nowTime - startTime
time = 24 * 60 ** 2 - time
rslt[2] = str(time % 60)
time = time // 60
rslt[1] = str(time % 60)
rslt[0] = str(time// 60)
print(rslt)
for i in range(3):
    if len(rslt[i]) < 2:
        rslt[i] = '0' + rslt[i]
print(rslt)
if rslt[0] == '24':
    print('00:00:00')
else:
    print(":".join(rslt))
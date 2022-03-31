n = int(input())

findSet = set()
data = dict()
for _ in range(n):
    a = int(input())
    if a in findSet:
        data[a] += 1
    else:
        data[a] = 1
    findSet.add(a)
max = 0
rslt = 0
for i in data.keys():
    if data[i] > max:
        rslt = i
        max = data[i]
    elif data[i] == max and rslt > i:
        rslt = i
print(rslt)

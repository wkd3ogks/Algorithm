# [Gold 4] 단어 수학
possible = [i for i in range(10)]
combine = [[] for _ in range(8)]
alphaCnt = [0 for i in range(26)]
alpha = [-1 for i in range(26)]
number = []
index = 0
n = int(input()) 
for _ in range(n):
    j = 0
    before = input()
    i = 8 - len(before)
    while i < 8:
        alphaCnt[ord(before[j]) - 65] += 1
        combine[i].append([before[j], index]) 
        j += 1
        i += 1
    index += 1
    number.append(0)
for i in range(8):
    for j in range(len(combine[i])):
       combine[i][j].append(alphaCnt[ord(combine[i][j][0]) - 65])
exponent = 7
for i in range(8):
    combine[i].sort(key=lambda x: -x[2])
    for alpha1, index, cnt in combine[i]:
        if alpha[ord(alpha1) - 65] == -1:
            alpha[ord(alpha1) - 65] = possible.pop() 
        number[index] += alpha[ord(alpha1) - 65] * 10 ** exponent
    exponent -= 1
total = 0
for i in number:
    total += i
print(total)




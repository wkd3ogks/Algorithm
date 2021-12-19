# [Gold 4] 문자열 폭발
# Stack + DP로 풀었다. 
string = input()
cmp = input()
length = len(cmp)
dpStack = [0]
stringStack = ['']
i = 0
for char in string:
    if char == cmp[dpStack[i]]:
        dpStack.append(dpStack[i] + 1)
    elif char == cmp[0]:
        dpStack.append(1)
    else:
        dpStack.append(0)
    stringStack.append(char)
    i += 1
    if length == dpStack[i]:
        for j in range(length):
            dpStack.pop()
            stringStack.pop()
        i -= length
if len(stringStack) == 1:
    print("FRULA")
else:
    for i in stringStack[1:]:
        print(i, end='') 
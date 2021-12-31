# [Gold 4] 부분합
# Two Pointer 문제 -> high, low 두개의 포인터를 해용해 푸는 문제

n, s = map(int, input().split())
seq = [0]
seq += list(map(int, input().split()))
low = 0
high = 0
sum = seq[0]
length = 100001
while low <= high and high < n:
    if sum > s:
        length = min(length, high - low + 1)
        sum -= seq[low]
        low += 1
    elif sum < s:
        high += 1
        sum += seq[high]
    else:
        length = min(length, high - low + 1)
        high += 1
        sum += seq[high]
if length == 100001:
    print(0)
else:
    print(length)

    



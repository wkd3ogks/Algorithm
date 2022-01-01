# [Gold 4] 부분합
# Two Pointer 문제 -> high, low 두개의 포인터를 해용해 푸는 문제

n, s = map(int, input().split())
seq = list(map(int, input().split()))
# low까지 뺀다
low = -1 
# high까지 더한다.
high = 0 
sum = seq[0] 
length = 100001
while low < high and high < n:
    if sum > s:
        length = min(length, high - low)
        low += 1
        if low < n:
            sum -= seq[low]
    elif sum < s:
        high += 1
        if high < n:
            sum += seq[high]
    else:
        length = min(length, high - low)
        high += 1
        if high < n:
            sum += seq[high]
print(length % 100001)

    



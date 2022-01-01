# [Gold 3] 소수의 연속합
# Two pointer로 풀어보자.
n = int(input())
prime = [i for i in range(n + 1)]
prime[0], prime[1] = 0, 0
primeList = []
length = 0
memoLeft = []
memoRight = []

# Max : 4,000,000
for i in range(2, n + 1):
    if prime[i] != 0:
        primeList.append(prime[i])
        length += 1
        for j in range(i + i, n + 1, i):
            prime[j] = 0
# Max : 4, 000, 000
for i in range(length):
    if i == 0:
        memoLeft.append(2)
    else:
        memoLeft.append(memoLeft[i - 1] + primeList[i])
for i in range(length - 1, -1, -1):
    if i == length - 1:
        memoRight.append(primeList[length - 1])
    else:
        memoRight.append(memoRight[length - 2 - i] + primeList[i])

print(primeList)
print(memoLeft)
print(memoRight)
left = 0
right = 0
total = memoLeft[length - 1] 
cnt = 0
while left <= right:
    if total == n:
        cnt += 1
    elif total:
        break




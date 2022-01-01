# [Gold 3] 소수의 연속합
# Two pointer로 풀어보자.
n = int(input())
prime = [i for i in range(n + 1)]
prime[0], prime[1] = 0, 0
memo = []
length = 0

# Max : 4,000,000
for i in range(2, n + 1):
    if prime[i] != 0:
        memo.append(prime[i])
        length += 1
        for j in range(i + i, n + 1, i):
            prime[j] = 0

left = -1
right = 0
if length >= 1:
    total = memo[0] 
    cnt = 0
    # Left < length 필요없는 이유는 lft < right가 있기에.
    # right < length가 필요한 이유는 마지막 까지 더해도 total < n일때 무한루프
    while left < right and right < length:
        if total < n: 
            right += 1
            if right < length:
                total += memo[right]
        elif total == n:
            cnt += 1
            left += 1
            if left < length:
                total -= memo[left]
        else:
            left += 1
            if left < length:
                total -= memo[left]
    print(cnt)
else:
    print(0)




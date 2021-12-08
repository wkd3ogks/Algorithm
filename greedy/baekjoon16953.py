# [Silver 1] a -> b
# 그리디로 푼 이유 : 끝 자리가 짝수가 아니라면 2로 나눠지지 않는다. 그래서 항상 1이 끝자리일때는 없애줘야한다.
# 또 1이 아니라면 무조건 -1을 출력해줘야한다.

n, m = map(int, input().split())

count = 1
while m > n:
    if str(m)[-1] == '1':
        m = int(str(m)[:-1])
    elif m % 2 == 0:
        m = m // 2
    else:
        break
    count += 1
if n == m:
    print(count)
else:
    print(-1) 

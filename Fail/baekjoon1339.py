# [Gold 4] 단어 수학
# 갯수에 가중치를 줘서(자릿수) 해결하면 되는 문제
# 살짝 운으로 풀은 느낌? 우연하게 생각함
# 숫자는 쪼갤 수 있다. 899 = 800 + 90 + 9, 교환법칙이 가능하다.(나중에 더해도 된다) A + B = B + A

n = int(input())
data = list()
alpha = [0 for _ in range(26)]
for _ in range(n):
    data.append(input())

for string in data:
    length = len(string) - 1
    for char in string:
        alpha[ord(char) - 65] += 10 ** length
        length -= 1
alpha.sort(reverse=True)
num = 9
total = 0
for i in alpha:
    total += i * num
    num -= 1
print(total)


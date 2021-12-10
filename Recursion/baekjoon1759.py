# [Gold 5] 암호 만들기

l, c = map(int, input().split())
alpha = input().split()
alpha.sort()
vowel = ['a', 'e', 'i', 'o', 'u']

def solve(alpha, cnt1, cnt2,result):
    if cnt1 + cnt2 == l:
        if cnt1 >= 1 and cnt2 >=2:
            for k in result:
                print(k, end='')
            print()
        return
    elif not alpha:
        return
    for i in range(len(alpha)):
        if alpha[i] in vowel:
            cnt1 += 1
            result.append(alpha[i])
            solve(alpha[i + 1:], cnt1, cnt2, result)
            cnt1 -= 1
            result.pop()
        else:
            cnt2 += 1 
            result.append(alpha[i])
            solve(alpha[i + 1:], cnt1, cnt2, result)
            cnt2 -= 1
            result.pop()

solve(alpha, 0, 0, [])

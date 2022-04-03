# [Silver 4] 좋은 단어

n = int(input())
cnt = 0
for _ in range(n):
    stack = []
    length = 0
    for char in input():
        stack.append(char)
        length += 1
        while length >= 2:
            if stack[length - 1] == stack[length - 2]:
                stack.pop()
                stack.pop()
                length -= 2
            else:
                break
    if not stack:
        cnt += 1
print(cnt)

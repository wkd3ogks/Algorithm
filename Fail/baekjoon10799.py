# [ Silver 3 ] 쇠막대기
from collections import deque

stack = []

userInput = deque(input())
inputLength = len(userInput)
lastIndex = 0
while userInput:
    stack.append(userInput.popleft())
    if stack[lastIndex] == ')':
        stack.pop()
        lastIndex -= 1
        while lastIndex >= 0:
            if stack[lastIndex] == '('
    lastIndex += 1
print(stack)
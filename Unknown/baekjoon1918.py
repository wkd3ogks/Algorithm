# [Gold 3] 후위 표기식
basicNotation = input()
stack = []
length = 0
for char in basicNotation:
    if 65 <= ord(char) and ord(char) <= 90:
        print(char,end='')
    else:
        stack.append(char)
        length += 1
    while length >= 2:
        if stack[length - 1] == '+' or stack[length - 1] == '-':
            if stack[length - 2] == '+' or stack[length - 2] == '-' or stack[length - 2] == '*' or stack[length - 2] == '/':
                print(stack.pop(-2), end='')
                length -= 1
            else:
                break
        elif stack[length - 1] == '*' or stack[length - 1] == '/':
            if stack[length - 2] == '*' or stack[length - 2] == '/':
                print(stack.pop(-2), end='')
                length -= 1
            else:
                break
        elif stack[length - 1] == ')':
            while stack[length - 1] != '(':
                temp = stack.pop()
                if temp != ")":
                    print(temp, end='')
                length -= 1
            stack.pop()
            length -= 1
            break
        else:
            break
while stack:
    print(stack.pop(), end='')        
# Stack으로 풀어보려 했는지 일반적인 규칙을 찾지 못한 건지 없는건지 모르겠음
# 그런데 분할정복의 방식은 확실한 규칙이 존재하는 것 같다.(더 쉬움)
# 근데 직접 그래프를 그리는 방식이 대체로 많은 풀이(어떻게 한거지?)

preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break

# left is rootNode index
def solve(left, right, preorder):
    rootNode = preorder[left]
    while left + 1 <= right:
        if 

    print(rootNode)

 


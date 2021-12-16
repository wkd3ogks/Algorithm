# [Gold 2] 트리의 순회
# Preorder : (Root) - (Left) - (Right)
# Inorder : (Left) - (Right) - (Root) 
# Postorder : (Left) - (Root) - (Right)
# TODO: 트리 다시 공부 및 분할정복 문제 쉬운 것 부터 풀기
n = int(input())
tree = [[] for _ in range(n)]
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

def solve():
    pass
def divide(inorder, root, postorder):
    print(root, inorder, postorder)
    left = []
    right = []
    if len(inorder) == 1:
        tree[root - 1].append(inorder[0] - 1)
    for i in range(len(inorder)):
        if inorder[i] == root:
            left = inorder[:i]
            right = inorder[i + 1:]
    for i in range(len(postorder)):
        if len(postorder) <= 2:
            break
        if postorder[i] not in left:
            print(postorder[i - 1])
            divide(left, postorder[len(postorder) - 1], postorder[:i])
            divide(right, postorder[len(postorder) - 1], postorder[i:])
            break
divide(inorder, postorder[n - 1], postorder)
print(tree)


# [Gold 2] 트리의 순회
# Preorder : (Root) - (Left) - (Right)
# Postorder : (Left) - (Right) - (Root) 
# inorder : (Left) - (Root) - (Right)
import sys
sys.setrecursionlimit(10**5 + 100)
n = int(input())
tree = [[] for _ in range(n)]

inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))
INF = 1000000
pos = [INF for _ in range(n + 1)]
for i in range(n):
    pos[inorder[i]] = i
def solve(ileft, iright, pleft, pright):
    global rslt
    # print(inorder[ileft: iright + 1], postorder[pleft: pright + 1])
    if ileft > iright:
        return 
    rootNode = postorder[pright]
    print(rootNode, end=' ')
    if ileft == iright:
        return
    solve(ileft, pos[rootNode] - 1, pleft, pleft + pos[rootNode] - ileft - 1)
    solve(pos[rootNode] + 1, iright, pleft + pos[rootNode] - ileft, pright - 1)

solve(0, n - 1, 0, n - 1)


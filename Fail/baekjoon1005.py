# [Gold 3] ACM Craft
# 시간을 음수로 바꿔서 최소 스패닝 트리
v, e = map(int, input().split())
unionSet = set()
edges = []
for _ in range(e):
    edges.append(list(map(int, input().split())))
edges.sort()
print(edges)

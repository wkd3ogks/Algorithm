# [Gold 1] 구슬 탈출 2
# 주의 : 구슬도 또 하나의 장애물이 될 수 있다. ex) x축 똑같을 때 y 축으로 이동시키면...
# y axis Standard
wallX = [[] for _ in range]  
# x axis Standard
wallY = [[] for _ in range]  
# Goal point
goal = [-1, -1]

n, m = map(int, input().split())
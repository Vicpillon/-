# https://www.acmicpc.net/problem/1697
import sys
from collections import deque

input = sys.stdin.readline

N, K = list(map(int, input().split()))
# 수빈 -> x-1, x+1 or 2*x
Max = 100001
q = deque()
q.append([N, 0])
visited = [0] * Max
visited[N] = 1
while(q):
    current, seconds = q.popleft()
    if current == K: # 동생 찾음
        print(seconds)
        break
    for i in (current-1, current+1, current*2):
        if 0 <= i < Max and visited[i] != 1:
            q.append([i, seconds+1])
            visited[i] = 1
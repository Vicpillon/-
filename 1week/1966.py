# https://www.acmicpc.net/problem/1966

# 큐의 요소들의 중요도를 파악해서 가장 높은 것부터 출력할 때, 특정 요소가 몇번째로 출력되는지 출력.
import sys
from collections import deque

input = sys.stdin.readline

T = int(input()) 

for t in range(T):
    N, M = list(map(int, input().split())) # 문서의 개수, 특정지을 문서 위치
    documents = list(map(int, input().split())) # 문서의 중요도

    # M이 출력되기 위한 조건 1. 현재 위치가 0 2. Max와 같은 우선순위 값
    q = deque(documents)
    printCounts = 0

    while q:
        Max = max(q)
        if Max > q[0]: # Max 우선순위보다 작을 경우
            q.append(q.popleft()) # 큐 맨 뒤로 보냄
        else: # Max 우선순위와 같을 경우
            printCounts += 1
            if M == 0:
                break
            q.popleft()
        
        M = M - 1 if M > 0 else len(q) -1  # 인덱스 조정

    print(printCounts)        
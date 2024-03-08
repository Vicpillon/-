# https://www.acmicpc.net/problem/1158

import sys

input = sys.stdin.readline

N, K = list(map(int, input().split()))
circle = [i for i in range(1, N+1)]
result = []
tmp = K-1

while(len(circle) > 0):
    result.append(circle[tmp])
    circle.pop(tmp)

    if tmp + K-1 >= len(circle): # tmp 인덱스가 circle 리스트를 초과할 경우
        if len(circle) == 0: # circle이 empty
            continue
        else:
            tmp = (tmp + K-1) % len(circle)
    else:
        tmp = tmp + K-1

# 출력
print('<', end="")
for i in result:
    print(i, end="")
    if i != result[-1]:
        print(', ', end="")
print('>')

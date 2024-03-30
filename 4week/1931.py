# https://www.acmicpc.net/problem/1931
import sys

input = sys.stdin.readline

N = int(input())
meeting = []

# O(N)
for i in range(N):
    start, end = map(int, input().split())
    meeting.append([start, end])

# 정렬 O(NlogN)
# 1. 종료 시간 오름차순 2. 시작 시간 오름차순
meeting.sort(key=lambda x:(x[1], x[0]))

count = 1
endTime = meeting[0][1] # 가장 먼저 배정된 회의의 종료 시간
# O(N)
for i in range(1, N):
    if meeting[i][0] >= endTime: # 이전 회의의 종료시간과 같거나 커야한다.
        count += 1
        endTime = meeting[i][1]

print(count)
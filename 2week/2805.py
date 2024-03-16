# https://www.acmicpc.net/problem/2805

import sys

input = sys.stdin.readline 

# 최소 M미터의 나무를 구하기 위해 설정할 절단기의 최대 높이 H
# 나무의 총 높이의 합은 M 이상

N, M = list(map(int, input().split())) 
heights = list(map(int, input().split()))

start = 1
end = max(heights) # 최장 나무 길이

while start <= end:
    mid = (start + end) // 2
    sum = 0 # 자른 나무의 총 길이
    
    for height in heights:
        if height >= mid:
            sum += height - mid
    if sum >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
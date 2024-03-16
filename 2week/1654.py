# https://www.acmicpc.net/problem/1654

import sys

input = sys.stdin.readline

# 문제의 시간복잡도는 O(K)이므로 O(N^2) 이하의 시간복잡도 알고리즘을 사용해야 한다.
# K개의 랜선을 각각 같은 길이이자 최대 길이로 N개 이상의 랜선으로 분리

K, N = list(map(int, input().split()))
lengths = [int(input()) for _ in range(K)]
start, end = 1, max(lengths)

while start <= end:
    mid = (start + end) // 2
    count = 0 # 잘린 랜선의 수

    for length in lengths:
        count += length // mid
    if count >= N: # 잘린 랜선의 수가 N 이상
        start = mid + 1
    else: # 잘린 랜선의 수가 N 미만
        end = mid - 1
print(end)
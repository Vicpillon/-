# https://www.acmicpc.net/problem/18870

import sys

input = sys.stdin.readline

N = int(input())
dots = list(map(int, input().split()))

# 시간복잡도 줄여야함. 일반 탐색은 안됨 => 최소 시간복잡도 O(NlogN)
# 주의점 1. 압축하려는 좌표보다 작은지 비교 2. 같은 좌표 여러개의 경우 중복카운트 x -> set

dots_set = sorted(set(dots)) # 정렬 O(nlogn)

dic = {dots_set[i]:i for i in range(len(dots_set))}
for i in dots: # O(1)씩 소요
    print(dic[i], end=' ')




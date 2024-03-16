# https://www.acmicpc.net/problem/1920

import sys

input = sys.stdin.readline

N = int(input())
ns = sorted(map(int, input().split()))
M = int(input())
ms = list(map(int, input().split()))

def binarySearch(arr, target, start, end): # 이진탐색
    if start > end:
        return 0
    
    mid = (start + end) // 2
    if arr[mid] == target:
        return 1
    elif arr[mid] > target:
        return binarySearch(arr, target, start, mid - 1)
    elif arr[mid] < target:
        return binarySearch(arr, target, mid + 1, end)

for m in ms:
    print(binarySearch(ns, m, 0, len(ns)-1))
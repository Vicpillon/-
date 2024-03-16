# https://www.acmicpc.net/problem/10816

import sys

input = sys.stdin.readline

N = int(input())
cards = sorted(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

dic = {}

for card in cards:
    if dic.get(card):
        dic[card] = dic.get(card) + 1
    else:
        dic[card] = 1

for num in nums:
    if dic.get(num):
        print(dic[num], end=" ")
    else:
        print(0, end=" ")
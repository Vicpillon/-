# https://www.acmicpc.net/problem/12845
import sys

input = sys.stdin.readline

# O(n)
n = int(input())
card = list(map(int, input().split())) 
gold = 0

card.sort(reverse=True) # 레벨 내림차순

for i in range(1, n):
    gold += card[0] + card[i]
print(gold)
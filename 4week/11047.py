# https://www.acmicpc.net/problem/11047
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coin = []
cnt = 0
for i in range(N):
    coin.append(int(input()))

coin.sort(reverse=True)

for i in range(N):
    if K:
        cnt += K // coin[i]
        K %= coin[i]

print(cnt)
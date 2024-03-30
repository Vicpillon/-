# https://www.acmicpc.net/problem/2875
import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

team = 0

while N + M - K >= 3 and N >= 2 and M >= 1:
    N -= 2
    M -= 1
    team += 1
print(team)
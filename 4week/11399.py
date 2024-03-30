# https://www.acmicpc.net/problem/11399
import sys

input = sys.stdin.readline

N = int(input())
people = list(map(int, input().split()))

# sort() => O(NlogN)
people.sort()
time = 0

mem = [0] * N
mem[0] = people[0]

# O(N)
for i in range(1, N):
    mem[i] = mem[i-1] + people[i]

print(sum(mem))

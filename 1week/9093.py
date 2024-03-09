# https://www.acmicpc.net/problem/9093

import sys 

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    sentence = input().split()
    
    for word in sentence:
        print(''.join(list(reversed(word))), end=" ")
# https://www.acmicpc.net/problem/10828
# 스택 구현 -> push, pop, size, empty, top

# 스택 -> 배열 or 링크드리스트
import sys

input = sys.stdin.readline

N = int(input())

stack = []

for i in range(N):
    command = input().split() 
    
    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

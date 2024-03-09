# https://www.acmicpc.net/problem/9012

# 올바른 괄호 쌍 문자열인지 판단
# 스택 -> push하다가 올바른 쌍을 만나면 같이 pop
import sys

input = sys.stdin.readline

T = int(input())

for t in range(T):
    stack = []
    arr = input()

    for i in arr:
        if '(' == i:
            stack.append(i)
        elif ')' == i:
            if stack and '(' == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
                break
    
    if stack: # 스택 안에 남아있는 것이 있다면
        print("NO")
    else:
        print("YES")
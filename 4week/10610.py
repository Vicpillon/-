# https://www.acmicpc.net/problem/10610
import sys

input = sys.stdin.readline

N = list(map(int, list(input().rstrip())))

# 0이 없을 경우 불가능
if 0 not in N:
    print(-1)
else:
    # 30의 최대 배수의 조건 -> 3 * 10 의 배수 -> 맨뒤에 0만 붙으면 3의 배수면 된다.
    # 맨앞은 최대한 큰 수, 맨 뒤는 0
    # 3의 배수 -> 모든 자리의 수의 합이 3의 배수
    # sum:O(N)
    if sum(N) % 3 == 0: # 모든 자리수의 합이 3의 배수
        N.sort(reverse=True) # O(NlogN)
        print("".join(map(str, N))) # map:O(logN), join:O(N)
    else:
        print(-1)
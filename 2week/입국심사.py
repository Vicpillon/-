# https://school.programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    start, end = 1, max(times) * n # 촤대 소요시간

    while start <= end:
        mid = (start + end) // 2 # 심사관 당 주어지는 시간
        people = 0 # 심사한 사람의 수
        for time in times:
            people += mid // time
            if people >= n: # 심사해야 할 사람의 수를 초과하면 바로 탈출
                break
        
        if people >= n: # 최소 n명을 심사 -> 시간이 적절하거나 넘침
            end = mid - 1
        else: # n명 미만으로 심사 -> 시간 부족
            start = mid + 1
    return start
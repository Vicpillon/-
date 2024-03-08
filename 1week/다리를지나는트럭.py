# https://school.programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    # 모든 트럭이 순서대로 다리를 건너기위해 필요한 시간
    # 선입선출 -> 큐
    # 트럭이 오를 때 1, 지날 때 bridge_length, 내릴 때 1.
    
    time = 0 # 초과한 시간
    passing = [] # 다리 위 트럭
    passed = [] # 다리를 지나간 트럭
    total = len(truck_weights) # 총 트럭의 수
    
    # 다리 위에 있을 수 있는 최대 트럭은 bridge_length 대 
    # (다리위 지속시간, 무게) 쌍으로 판별해서 반복문 돌리기

    while(len(passed) != total):
        # 트럭이 다리 아래로 내려감
        if passing and passing[0][0] == bridge_length: # 트럭이 다리 위에 있는 시간
            passed.append(passing[0][1])
            passing.pop(0)
        # 다리 위 트럭 지나는 중
        for i in range(len(passing)):
            passing[i][0] = passing[i][0] + 1 # 다리 위를 지나는 시간+1
        # 트럭이 다리 위로 올라감
        if truck_weights and sum(t[1] for t in passing) + truck_weights[0] <= weight: # 무게 초과 x
                passing.append([1, truck_weights.pop(0)])      
        time = time + 1
        
    return(time)


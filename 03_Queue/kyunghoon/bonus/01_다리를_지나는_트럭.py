from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    current_weight = 0

    while trucks:
        current_weight -= bridge.popleft()
        answer += 1

        if current_weight + trucks[0] > weight:
            bridge.append(0)
        else:
            next_truck = trucks.popleft()
            bridge.append(next_truck)
            current_weight += next_truck

    answer += bridge_length
    return answer

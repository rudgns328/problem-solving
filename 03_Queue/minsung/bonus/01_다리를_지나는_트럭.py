from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge_weight = 0

    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)

    while bridge:
        time += 1
        bridge_weight -= bridge.popleft()

        if trucks:
            if bridge_weight + trucks[0] <= weight:
                truck = trucks.popleft()
                bridge.append(truck)
                bridge_weight += truck
            else:
                bridge.append(0)

    return time

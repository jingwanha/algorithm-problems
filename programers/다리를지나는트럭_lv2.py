def solution(bridge_length, weight, truck_weights):
    answer = 0
    on_bridge = []

    while True:
        if len(on_bridge) >= bridge_length: on_bridge.pop(0)

        if len(truck_weights) == 0:
            answer+=bridge_length
            break

        if sum(on_bridge) + truck_weights[0] <= weight:
            on_bridge.append(truck_weights.pop(0))
        else:
            on_bridge.append(0)

        answer += 1

    return answer

if __name__=='__main__':
    bridge_length = 100
    weight = 100
    truck_weights = [10,10,10,10,10,10,10,10,10,10]

    res = solution(bridge_length, weight, truck_weights)
    print(res)


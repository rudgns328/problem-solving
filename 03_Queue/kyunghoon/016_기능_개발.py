def solution(progresses, speeds):
    answer = []
    days = [-(-(100 - p) // s) for p, s in zip(progresses, speeds)]

    deploy_day = 0
    for d in days:
        if d > deploy_day:
            answer.append(1)
            deploy_day = d
        else:
            answer[-1] += 1

    return answer

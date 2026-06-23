def solution(tickets):
    tickets.sort()
    answer = [False] * len(tickets)
    visited = ["ICN"]

    def dfs(start):
        if len(visited) == len(tickets) + 1:
            return True

        for i, (f, t) in enumerate(tickets):
            if f == start and not answer[i]:
                answer[i] = True
                visited.append(t)

                if dfs(t):
                    return True

                answer[i] = False
                visited.pop()

        return False

    dfs("ICN")
    return visited

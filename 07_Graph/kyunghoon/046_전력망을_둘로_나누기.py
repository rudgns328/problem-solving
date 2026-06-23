def solution(n, wires):
    visited = set()
    answer = 100
    count = 0
    graph = [[] for _ in range(n + 1)]

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    def cut_edge(i):
        nonlocal answer
        nonlocal count
        nodes = graph[i][:]
        for node in nodes:
            graph[i].remove(node)
            graph[node].remove(i)
            cnt = dfs(i)
            graph[i].append(node)
            graph[node].append(i)
            count = abs(2 * cnt - n)
            answer = min(count, answer)
            count = 0
            visited.clear()

    def dfs(i):
        visited.add(i)
        cnt = 1
        for v in graph[i]:
            if v not in visited:
                cnt += dfs(v)
    
        return cnt

    for i in range(1, n + 1):
        cut_edge(i)
    
    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
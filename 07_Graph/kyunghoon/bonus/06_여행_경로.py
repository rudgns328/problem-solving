from collections import defaultdict

def solution(tickets):
    answer = ["ICN"]
    graph = defaultdict(list)
    for k, v in tickets:
        graph[k].append(v)
    
    for key in graph:
        graph[key].sort()
        
        
    def dfs(start):
        if len(answer) == len(tickets) + 1:
            return True
        
        for i in range(len(graph[start])):
            next_node = graph[start].pop(i)
            answer.append(next_node)
            if dfs(next_node):
                return True
            graph[start].insert(i, next_node)
            answer.pop()
        
    dfs("ICN")
    return answer
from heapq import heappush, heappop

INF = 10**9

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]
    for u, v, w in fares:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    def dijkstra(start):
        dist = [INF] * (n + 1)
        dist[start] = 0
        heap = [(0, start)]
        
        while heap:
            cost, node = heappop(heap)
            
            if dist[node] < cost:
                continue
            
            for next_node, weight in graph[node]:
                new_cost = cost + weight
                if dist[next_node] > new_cost:
                    dist[next_node] = new_cost
                    heappush(heap, (new_cost, next_node))
        
        return dist
    
    s_dist = dijkstra(s)
    a_dist = dijkstra(a)
    b_dist = dijkstra(b)
    
    return min(s_dist[k] + a_dist[k] + b_dist[k] for k in range(1, n + 1))
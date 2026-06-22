from heapq import heappush, heappop

INF = 10**9

def solution(board):
    rows, cols = len(board), len(board[0])
    cost_map = [[[INF] * 4 for _ in range(rows)] for _ in range(cols)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    priority_queue = [(0, 0, 0, None)]

    while priority_queue:
        cost, r, c, direction = heappop(priority_queue)
        
        if (r, c) == (rows - 1, cols -1):
            return cost
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != 1:
                if direction is None or direction == (dr, dc):
                    new_cost = cost + 100
                else:
                    new_cost = cost + 600
                    
                d_idx = directions.index((dr, dc))    
                if new_cost < cost_map[nr][nc][d_idx]:
                    cost_map[nr][nc][d_idx] = new_cost
                    heappush(priority_queue, (new_cost, nr, nc, (dr, dc)))
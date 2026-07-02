def solution(board):
    box_check = [set() for _ in range(9)]
    row_check = [set() for _ in range(9)]
    col_check = [set() for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                box_row = i // 3
                box_col = j // 3
                box_check[box_row * 3 + box_col].add(board[i][j])
                row_check[i].add(board[i][j])
                col_check[j].add(board[i][j])
                
    def next_cell(row, col):
        if col + 1 < 9:
            return row, col + 1
        else:
            return row + 1, 0
        
    def backtrack(row, col):
        if row == 9:
            return True
        
        if board[row][col] != 0:
            nr, nc = next_cell(row, col)
            return backtrack(nr, nc)

        box_idx = (row // 3) * 3 + (col // 3)
        for i in range(1, 10):
            if i not in box_check[box_idx] and i not in row_check[row] and i not in col_check[col]:
                board[row][col] = i
                box_check[box_idx].add(i)
                row_check[row].add(i)
                col_check[col].add(i)
                
                nr, nc = next_cell(row, col)
                if backtrack(nr, nc):
                    return True
                
                board[row][col] = 0
                box_check[box_idx].remove(i)
                row_check[row].remove(i)
                col_check[col].remove(i)
                
        return False
    
    backtrack(0, 0)
    
    return board
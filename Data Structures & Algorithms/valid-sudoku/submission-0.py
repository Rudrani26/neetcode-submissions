class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #hashmap for rows, columns and squares
        rows_hash = defaultdict(set)
        columns_hash = defaultdict(set)
        squares_hash = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows_hash[r] 
                    or board[r][c] in columns_hash[c] 
                    or board[r][c] in squares_hash[(r // 3, c // 3)]):
                    return False
                    
                rows_hash[r].add(board[r][c])
                columns_hash[c].add(board[r][c])
                squares_hash[(r // 3, c //3)].add(board[r][c])

        return True



        
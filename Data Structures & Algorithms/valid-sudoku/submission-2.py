class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
        
                val = int(board[r][c])

                mask = 1 << val

                box_idx = (r // 3) * 3 + (c // 3)

                if (rows[r] & mask) or (cols[c] & mask) or (squares[box_idx] & mask):
                    return False
                
                rows[r] |= mask
                cols[c] |= mask
                squares[box_idx] |= mask
        
        return True



        
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [0] * n
        ans = []
        self.putQueen(0, board, ans)
        return ans
    
    def putQueen(self, row, board, ans):
        if row >= len(board):
            ans.append(self.draw(board))
            return
        for col in range(len(board)):
            if self.ok(row, col, board):
                board[row] = col
                self.putQueen(row + 1, board, ans)
                
                
    def draw(self, board):
        return [''.join(['Q' if i == col else '.' for i in range(len(board))]) for col in board]
        
    def ok(self, row, col, board):
        leftupcol = col - 1
        rightupcol = col + 1
        for idx in reversed(range(row)):
            if board[idx] == col:
                return False
            if leftupcol >= 0 and board[idx] == leftupcol:
                return False
            if rightupcol < len(board) and board[idx] == rightupcol:
                return False
            leftupcol -= 1
            rightupcol += 1
        return True

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        parents = list(range(m * n))
        
        def union(i, j):
            parents[find(i)] = find(j)
            
        def find(i):
            if parents[i] != i:
                parents[i] = parents[find(parents[i])]
            return parents[i]
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]     
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == 'O':
                    curPos = i * n + j
                    for dx, dy in directions:
                        adjI = i + dx
                        adjJ = j + dy
                        if board[adjI][adjJ] == 'O':
                            adjPos = adjI * n + adjJ
                            union(curPos, adjPos)
        
        borderSet = set()
        for i in range(m):
            if board[i][0] == 'O':
                borderSet.add(find(i * n))
            if board[i][n - 1] == 'O':
                borderSet.add(find(i * n + n - 1))
        for j in range(n):
            if board[0][j] == 'O':
                borderSet.add(find(j))
            if board[m - 1][j] == 'O':
                borderSet.add(find((m - 1) * n + j))
        
        for i in range(m):
            for j in range(n):
                if find(i * n + j) not in borderSet:
                    board[i][j] = 'X'

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        maxWidth = 0
        table = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if (matrix[i - 1][j - 1] == '1'):
                    table[i][j] = min(table[i][j - 1], table[i - 1][j], table[i - 1][j - 1]) + 1
                    maxWidth = max(maxWidth, table[i][j])
                    
        return maxWidth ** 2

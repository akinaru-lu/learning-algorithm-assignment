class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        table = [1, 1] + [0] * (len(s) - 1)
        for i in range(2, len(s) + 1):
            if 0 < int(s[i-1:i]) <= 9:
                table[i] += table[i - 1]
            if 10 <= int(s[i-2:i]) <= 26:
                table[i] += table[i - 2]
        return table[-1]

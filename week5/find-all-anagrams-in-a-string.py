class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def makeTable(s):
            table = [0] * 26
            for c in s:
                table[ord(c) - ord('a')] += 1
            return table
        
        target = makeTable(p)
        lenP = len(p)
        ans = []
        table = makeTable(s[:lenP])
        for tail in range(lenP, len(s)):
            if table == target:
                ans.append(tail - lenP)
            oldChar, newChar = s[tail - lenP], s[tail]
            table[ord(oldChar) - ord('a')] -= 1
            table[ord(newChar) - ord('a')] += 1
        if table == target:
            ans.append(len(s) - lenP)
        return ans

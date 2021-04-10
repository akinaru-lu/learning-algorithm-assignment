class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        ans = ""
        for i in range(1, len(s)):
            sub1 = self.expandAroundCenter(s, i - 1, i)
            sub2 = self.expandAroundCenter(s, i, i)
            maxSub = sub1 if len(sub1) > len(sub2) else sub2
            if len(maxSub) > len(ans):
                ans = maxSub
        return ans
        
    def expandAroundCenter(self, s, l, r) -> str:
        ans = ""
        while l >= 0 and r < len(s) and s[l] == s[r]:
            ans = s[l : r + 1]
            l -= 1
            r += 1
        return ans

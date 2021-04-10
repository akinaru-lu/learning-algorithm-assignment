class Solution:
    def isIsomorphic(self, s, t):
        def helper(s, t):
            mapping = dict()
            for i, j in zip(s, t):
                if i in mapping and mapping[i] != j:
                    return False
                mapping[i] = j
            return True
        
        return helper(s, t) and helper(t, s)

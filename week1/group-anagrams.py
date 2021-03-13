class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = collections.defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            memo[key].append(s)
        return memo.values()
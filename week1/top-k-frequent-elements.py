class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        memo = {}
        for n in nums:
            memo[n] = memo.get(n, 0) + 1
        h = []
        for n, freq in memo.items():
            heapq.heappush(h, (-freq, n))
        ans = [None] * k
        for i in range(k):
            ans[i] = heapq.heappop(h)[1]
        return ans

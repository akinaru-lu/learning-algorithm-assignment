class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0] * (num + 1)
        for i in range(num + 1):
            # x 是偶数：在 x >> 1 的末尾添0，和 x 有相同的1个数：ans[i] = ans[i >> 1]
            # x 是奇数：减掉1按偶数算再加回来：ans[i] = ans[(i - 1) >> 1] + 1 = ans[i >> 1] + 1
            ans[i] = ans[i >> 1] + (i & 1)
        return ans

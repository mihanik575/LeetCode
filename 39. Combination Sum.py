class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        #
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):

            for d in nums:
                if i >= d: dp[i] += dp[i - d]

        return dp[target]
class Solution(object):
    def subarraySum(self, nums, k):
        res = 0
        curSum = 0
        prefixSums = {0: 1}

        for n in nums:
            curSum += n
            diff = curSum - k
            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = prefixSums.get(curSum, 0) + 1

        return res
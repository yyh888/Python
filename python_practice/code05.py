class Solution(object):
    def IsPrime(self, num):
        if (num < 2):
            return False
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                return False
        return True

    def diagonalPrime(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        iRes = 0
        for i in range(len(nums)):
            if self.IsPrime(nums[i][i]):
                iRes = max(iRes, nums[i][i])

        for i in range(len(nums[0])):
            if self.IsPrime(nums[i][len(nums[0]) - i - 1]):
                iRes = max(iRes, nums[i][len(nums[0]) - i - 1])
        return iRes
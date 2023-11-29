class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        firstNum = -1
        idx = -1
        secondNum = -1
        for i in range(len(nums)):
            if firstNum < nums[i]:
                secondNum = firstNum
                firstNum = nums[i]
                idx = i
            elif secondNum < nums[i]:
                secondNum = nums[i]
        if idx == -1 or firstNum < secondNum * 2:
            return -1
        else:
            return idx
# class Solution(object):
#     def findLengthOfLCIS(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         res = 1
#         ret = 1
#         for i in range(1, len(nums)):
#             if nums[i] > nums[i - 1]:
#                 ret += 1
#                 res = max(res, ret)
#             else:
#                 ret = 1
#         return res
n = 10
dp = [10 for i in range(n)]
print(dp)
'''
628. Maximum Product of Three Numbers
Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6
'''

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        return max(
            nums[-1] * nums[-2] * nums[-3],  # three largest
            nums[0] * nums[1] * nums[-1]     # two smallest and largest
        )

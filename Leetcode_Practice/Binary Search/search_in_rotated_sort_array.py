'''
33. Search in Rotated Sorted Array

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
'''

class Solution(object):
    def search(self, nums, target):
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = low + (high-low)//2

            if nums[mid] == target : return mid #if mid is targeet return directly

            if nums[low] <= nums[mid] :   # first half
                if nums[low] <= target < nums[mid] :
                    high = mid - 1
                else : 
                    low = mid + 1

            else :      # second half
                if nums[mid] < target <= nums[high] :
                    low = mid + 1
                else :
                    high = mid - 1
        return  -1

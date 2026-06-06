'''
2574. Left and Right Sum Differences

Example 1:

Input: nums = [10,4,8,3]
Output: [15,1,11,22]
Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

Example 2:

Input: nums = [1]
Output: [0]
Explanation: The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].
'''
class Solution(object):
    def leftRightDifference(self, nums):

        total = sum(nums)
        leftsum = 0
        ans = []

        for i in nums:
            rightsum = total - leftsum - i
            ans.append(abs(leftsum-rightsum))
            leftsum += i


        return ans

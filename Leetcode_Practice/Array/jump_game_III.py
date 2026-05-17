'''
1306. Jump Game III
Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 
Example 2:

Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true 
Explanation: 
One possible way to reach at index 3 with value 0 is: 
index 0 -> index 4 -> index 1 -> index 3
'''

class Solution(object):
    def canReach(self, arr, start):
        visited = set()

        def dfs(i):
            # Out of bounds or already visited
            if i < 0 or i >= len(arr) or i in visited:
                return False

            # Reached value 0
            if arr[i] == 0:
                return True

            visited.add(i)

            # Jump forward or backward
            return dfs(i + arr[i]) or dfs(i - arr[i])

        return dfs(start)

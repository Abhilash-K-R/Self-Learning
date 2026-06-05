'''
344. Reverse String
Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l , r = 0 , len(s)-1

        while l < r :
            s[l] , s[r] = s[r] , s[l]
            l +=1
            r -=1

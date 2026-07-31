'''
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]      # initial prefix set to 1st 

        for s in strs[1:]:          # check all strings exept 1st
            while not s.startswith(prefix):    # if string not start with prefix , remove the last letter from prefix and try upto ""
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix

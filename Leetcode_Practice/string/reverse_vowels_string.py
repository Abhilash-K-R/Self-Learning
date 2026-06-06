'''
345. Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:
Input: s = "leetcode"
Output: "leotcede"
'''

class Solution(object):
    def reverseVowels(self, s):
        s = list(s) 
        l, r = 0, len(s)-1

        while l<r:
            if s[l] in "aeiouAEIOU":
                while l<r and s[r] not in "aeiouAEIOU":
                    r -=1
                s[l], s[r] = s[r],s[l]
                r -=1
            l +=1

        return "".join(s)

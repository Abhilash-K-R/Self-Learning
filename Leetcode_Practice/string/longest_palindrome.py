class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        
        length = 0
        odd = False
        
        for freq in count.values():
            if freq % 2 == 0:
                length += freq
            else:
                length += freq - 1
                odd = True
        
        if odd:
            length += 1
        
        return length

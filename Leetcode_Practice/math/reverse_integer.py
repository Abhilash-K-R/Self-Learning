'''
7. Reverse Integer
Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
'''

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1  # assign sign
        x = abs(x) # convert positive

        rev = int(str(x)[::-1]) #reverse

        rev *=sign # handels sign - or +

        if rev < -2**31 or rev > 2**31 - 1:  # manage limits
            return 0

        return rev 

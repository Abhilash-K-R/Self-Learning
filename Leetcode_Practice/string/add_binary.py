'''
67. Add Binary
Given two binary strings a and b, return their sum as a binary string.
Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''

# code in leetcode
class Solution(object):
    def addBinary(self, a, b):
        a = int(a, 2)
        b = int(b, 2)

        s = a + b

        return bin(s)[2:]

  '''
Explanation

int(a, 2) → converts binary string to decimal.
int(b, 2) → converts binary string to decimal.
a + b → adds the numbers.
bin(s) → converts decimal back to binary (e.g., '0b1010').
[2:] → removes the '0b' prefix.
'''

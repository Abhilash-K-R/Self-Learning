'''
17. Letter Combinations of a Phone Number

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]
 '''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        phone = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        result = [""]
        for i in digits:
            new = []

            for com in result:
                for let in phone[i]:
                    new.append(com+let)

            result = new

        return result

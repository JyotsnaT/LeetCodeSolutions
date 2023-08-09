# Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

## Solution 1

    class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_char = {'2' : ["a",'b','c'],
        '3' : ["d",'e','f'],
        '4' : ["g",'h','i'],
        '5' : ["j",'k','l'],
        '6' : ["m",'n','o'],
        '7' : ["p",'q','r', 's'],
        '8' : ["t",'u','v'],
        '9' : ["w",'x','y', 'z']}


        def perms(str1):
            nonlocal digit_to_char
            output_perms = []

            if str1 != "":
                last_element = str1[-1]
                prefix_perms = perms(str1[:-1])
                for char in digit_to_char[last_element]:
                    for perm in prefix_perms:
                        output_perms.append(perm+char)
            if len(str1) == 1:
                output_perms = digit_to_char[str1]
            return output_perms
        
        return perms(digits)

- Runtime : 47sec Beats 29.07%of users with Python3
- Memory : 16.38mb Beats 53.03%of users with Python3
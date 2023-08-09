# [Minimum Flips to Make a OR b Equal to c](https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/description)

# Solution 1
Based on BitWise Manipulation
    
    class Solution:
        def minFlips(self, a: int, b: int, c: int) -> int:
            if a | b == c:
                return 0
                
            a_temp = a
            b_temp = b
            c_temp = c
    
            flip_counter = 0
            while(a_temp > 0 or b_temp > 0 or c_temp > 0):
                bit_a = a_temp & 1
                bit_b = b_temp & 1
                bit_c = c_temp & 1
                if bit_c:
                    if (bit_a | bit_b) != bit_c:
                        flip_counter += 1
                else:
                    flip_counter += bit_a + bit_b
                a_temp = a_temp >> 1
                b_temp = b_temp >> 1
                c_temp = c_temp >> 1
            
            return flip_counter
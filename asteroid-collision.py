'''
Author : Jyotsna

This function finds out the state of sequence of asteroids represented by their size and direction after their collision
'''

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for aster in asteroids:
            if not stack or stack[-1]*aster > 0 or stack[-1] * -1 >0:
                stack.append(aster)
            else:
                while stack and stack[-1]*aster < 0 and abs(stack[-1]) < abs(aster):
                    stack.pop()
                if not stack or stack[-1]*aster > 0:
                    stack.append(aster)
                elif abs(stack[-1]) == abs(aster):
                    stack.pop()
                else:
                    continue
        
        return stack
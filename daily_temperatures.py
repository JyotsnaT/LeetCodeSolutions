class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        answers = [0]*N
        # Solution 1 : Brute force
        # for i in range(N):
        #     for j in range(i+1, N):
        #         if temperatures[j] > temperatures[i]:
        #             answers[i] = j-i
        #             break

        # Solution 2 : using stack

        stack = []
        stack.append(N-1)

        for i in range(N-2, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                answers[i] = stack[-1]-i
            stack.append(i)
        
        return answers

## Solution 1

    class Solution:
        def uniquePaths(self, m: int, n: int) -> int:
            unique_paths = [[1]*n]*m

        for i in range(1,m):
            for j in range(1,n):
                top_paths = unique_paths[i-1][j] if i>0 else 0
                side_paths = unique_paths[i][j-1] if j>0 else 0
                unique_paths[i][j] = top_paths + side_paths

        return unique_paths[-1][-1]

 - Runtime
36ms
Beats 92.63%of users with Python3

 - Memory
16.12mb
Beats 96.27%of users with Python3
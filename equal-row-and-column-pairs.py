'''
Author : Jyotsna
This function has a solution to Equal Row and Column Pairs.

Algorithm used - hash functions
'''

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pairs = 0
        col_hash = []
        for i in range(n):
            col = grid[i]
            # print(col)
            col_hash.append(",".join([str(x) for x in col]))

        row_hash = []
        for j in range(n):
            row = []
            for k in range(n):
                row.append(grid[k][j])
            row_hash.append(",".join([str(x) for x in row]))

        for ch in col_hash:
            # print(ch)
            ch_finds = [x for x in row_hash if x == ch]
            pairs += len(ch_finds)
        
        return pairs
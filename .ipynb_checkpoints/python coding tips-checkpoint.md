# Tips while coding leetcode solutions in python3

1. In order to create a 2D array do not initialize the 2D array like this

       two_d_arr = [[0]*n]*m

   This is the easiest and most convinient way to create a 2D array. However, it might be wrong and would not give you the desired results. The reason is when you create a 2D array by multiplying an instance of 1D array m times, m copies of identical arrays are not created, instead a reference to the same array is created. Which results in all the rows getting modified when you try to modify just 1. Specially applicable if you are trying to solve DP problems.

   The correct way to do it however is to use nested list comprehension like this

       two_d_arr = [[0 for i in range(n)] for j in range(m)]
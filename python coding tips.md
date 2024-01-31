# Tips while coding leetcode solutions in python3

1. In order to create a 2D array do not initialize the 2D array like this

       two_d_arr = [[0]*n]*m

   This is the easiest and most convinient way to create a 2D array. However, it might be wrong and would not give you the desired results. The reason is when you create a 2D array by multiplying an instance of 1D array m times, m copies of identical arrays are not created, instead a reference to the same array is created. Which results in all the rows getting modified when you try to modify just 1. Specially applicable if you are trying to solve DP problems.

   The correct way to do it however is to use nested list comprehension like this

       two_d_arr = [[0 for i in range(n)] for j in range(m)]

2. While doing binary search, compute mid like this

        mid = left + (right - left)//2
   and not

       mid = (left + right)//2
   The first one takes care of all the integer overflow scenarios, that might occur in the second case.

3. While testing the codes for bugs, keep these scenarios in mind

      
4. Steps of code verification
    - Code review
      Code review checklist
        - variable names consistency
        - spelling mistake in variable names, function names, operator names
        - Code hot spots. High risk lines in code
            - Math
            - Moving indices
            - Base cases
            - Parameters when calling recursion
            - 2D array indices
        - Readability
            - Can if be replaced with terenary operator?
        - Logical checks
            - Whenever there is a while loop or recursive function, make sure they are not going into infinite loop.
            - The while loop should have proper increment or decrememt of loop variable and definite stop condition
            - The recursive function should have a base case defined for the recursion to stop.
            - The variable names should be consistent across. The right variable should be used while assignment or evaluation.
            -  
    - Test cases
        - Start with small example
        - Edge cases
            - nulls, empty string, single element
            - all punctuation, all duplicates, sorted strings
        - Big test case (optional)
    - Do not reverify the algorithm, but dry run the code line by line.
    - Do not blind test, but also verify the partial values
    - Do not do quick and sloppy fixes like flipping values randomly, but instead go through the problem solution properly.
  
6. HashMap search. Do not find an element in hash map like this

        isPresent = item in hash_dict.keys()
   but do this

        isPresent = item in hash_dict
   The first one will fetch the list of keys from the hash map and then perform a linear search, which will be done in O(n) and hence defeat the purpose of using a hashmap. The second search is guarenteed to be done in O(1). 
           
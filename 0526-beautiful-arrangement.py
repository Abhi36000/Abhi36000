class Solution:
    def countArrangement(self, n: int) -> int:
        # Initialize a list of integers from 1 to n
        nums = list(range(1, n+1))
        self.count = 0
        
        # Define a recursive function to generate all possible permutations
        def backtrack(start):
            # Base case: If all elements have been permuted, increment the count
            if start == n:
                self.count += 1
            # Recursive case: Generate all possible permutations
            for i in range(start, n):
                # Swap the current element with the start element
                nums[start], nums[i] = nums[i], nums[start]
                # Check if the current permutation is beautiful
                if nums[start] % (start+1) == 0 or (start+1) % nums[start] == 0:
                    # Recurse with the next element
                    backtrack(start+1)
                # Swap the current element back to restore the original list
                nums[start], nums[i] = nums[i], nums[start]
        
        # Call the recursive function with the first element
        backtrack(0)
        return self.count
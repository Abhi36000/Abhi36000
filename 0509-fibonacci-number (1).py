class Solution:
    def fib(self, n: int) -> int:
        memo = [0,1]
        if n <= 1 :
            return n
        for i in range( 2, n+1 ):
            memo.append( memo[i-1] + memo[i-2] )
        return memo[-1]        
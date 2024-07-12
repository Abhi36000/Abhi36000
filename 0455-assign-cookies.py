class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        # to keep a track of the number of children
        output = 0
        # to traverse along the array g
        j = 0
        for i in range(len(s)):
            if g[j] <= s[i]: # given condition
                j = j + 1
                output = output + 1
            # stop checking when the entire array g is traversed
            if j == len(g):
                break
        
        return output
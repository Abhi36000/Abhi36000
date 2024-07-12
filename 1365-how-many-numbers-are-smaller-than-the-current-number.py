class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
      d = {}
      for index,value in enumerate(sorted(nums)):
        if value not in d:
          d[value] = index
          
      ans = [d[value] for value in nums]
      return ans
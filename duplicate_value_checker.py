from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
     heap=set()
     for i in nums:
       if i in heap:
         return True
       heap.add(i)
     return False



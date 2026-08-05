class Solution:
    import math
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

   
        low = 0
        high = len(numbers) - 1
        
        i = 0
        while(numbers[low] + numbers[high] != target):
            if numbers[low] + numbers[high] > target:
                high -= 1
            else:
                low += 1
            i += 1

        return [low + 1, high + 1]
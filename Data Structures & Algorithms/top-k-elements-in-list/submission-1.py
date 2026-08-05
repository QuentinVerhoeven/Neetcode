class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #How this works:
        # create a list where index is a frequency, and at each index
        #store the numbers that appear that many times
        #
        # Build a map that counts how many times each number appears so we
        # can do the above
        #
        #
        counts = {}
        frequencies = [[] for i in range(len(nums) + 1)] 
        #we need +1 b/c an item can appear n times
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        for num, counts in counts.items(): 
            frequencies[counts].append(num)
        result = []

        for i in range(len(frequencies) - 1, 0, -1):
            for num in frequencies[i]:
                result.append(num)
                if len(result) == k:
                    return result
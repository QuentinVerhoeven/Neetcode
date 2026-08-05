class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        #map number to index
        for i in range(len(nums)):
            map[nums[i]] = i

        for i in range(len(nums)):
            numNeeded = target - nums[i]
            if map.get(numNeeded, -1) != -1:
                returnArray = [i, map[numNeeded]] if i < map[numNeeded] else map[numNeeded, i]
                return returnArray

            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        #map number to index
        for i in range(len(nums)):
            map[list[i]] = i

        for i in range(len(nums)):
            numNeeded = target - nums[i]
            if map.get(numNeeded, -1) != -1:
                if i < map[numNeeded]:
                    return [1, map[numNeeded]]
                else:
                    return [map[numNeeded], 1]

            
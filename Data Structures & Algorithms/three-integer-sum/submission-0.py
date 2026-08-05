class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        

        for i in range(len(nums)):
            if i != 0:
                if nums[i] == nums[i -1]:
                    continue
            first = i + 1
            second = len(nums) - 1
            while first < second:
                sum = nums[i] + nums[first] + nums[second]
                if sum == 0:
                    result.append((nums[i], nums[first], nums[second]))
                    first += 1
                    second -= 1
                    while nums[first] == nums[first - 1] and first < second:
                        first += 1
                elif sum > 0:
                    second -= 1
                else:
                    first += 1

        return result
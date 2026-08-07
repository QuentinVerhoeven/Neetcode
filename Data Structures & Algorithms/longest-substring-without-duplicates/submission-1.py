class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        MAX = 0
        l, r = 0,0
        characters = set()

        while r < len(s):
            while s[r] in characters:
                characters.remove(s[l])
                l += 1
            MAX = max(MAX, r - l + 1)
            characters.add(s[r])
            r+=1
        return MAX

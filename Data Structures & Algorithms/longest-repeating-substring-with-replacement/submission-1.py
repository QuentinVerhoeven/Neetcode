class Solution:
    #BY MYSELF kindof (not fully)
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0,0
        MAX = 0
        char_set = {}


        #number of changes is really the window - max character


        while r < len(s):
            char_set[s[r]] = char_set.get(s[r], 0) + 1 
            max_val = max(char_set.values())
            #gets key with max value

            if (r - l + 1) - max_val > k:
                char_set[s[l]] -= 1
                l += 1
            
            MAX = max(MAX, r - l + 1)
            r += 1


        return MAX
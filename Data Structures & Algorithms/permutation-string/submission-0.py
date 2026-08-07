class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False


        #we need to keep track of number of times char appears
        s1_map = {}
        s2_map = {}
        for i in range(len(s1)):
            s1_map[s1[i]] = s1_map.get(s1[i], 0) + 1
            s2_map[s2[i]] = s2_map.get(s2[i], 0) + 1

        l, r = 0, len(s1) -1 
        if s1_map == s2_map:
                return True
        while r < len(s2) - 1:
            if s1_map == s2_map:
                return True

            if s2[l] in s2_map: 
                s2_map[s2[l]] -= 1
            
            if s2[r+1] in s2_map:
                s2_map[s2[r + 1]] += 1
            else:
                s2_map[s2[r+1]] = 1
            if s2_map[s2[l]] == 0:
                del s2_map[s2[l]]
            if s1_map == s2_map:
                return True
            r += 1
            l += 1


        
        return False



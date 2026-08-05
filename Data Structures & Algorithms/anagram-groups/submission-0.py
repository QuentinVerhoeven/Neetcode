class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = defaultdict(list)
        for string in strs:
            sortedStr = ''.join(sorted(string))
            myMap[sortedStr].append(string)
        return list(myMap.values())
            
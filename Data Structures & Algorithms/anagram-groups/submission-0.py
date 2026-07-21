class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        count = 0
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord("a")] += 1
            
            hashmap[tuple(count)].append(s)

        return [values for key,values in hashmap.items()]
            



        
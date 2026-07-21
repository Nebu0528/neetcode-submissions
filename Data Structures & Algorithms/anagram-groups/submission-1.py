class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #see which characters have matching counts, append them as a tuple in the array

        hashmap = defaultdict(list)

        for c in strs:
            count = [0] * 26
            for i in c:
                count[ord(i)-ord('a')] += 1
            hashmap[tuple(count)].append(c)
        
        return [values for key,values in hashmap.items()]

            



        
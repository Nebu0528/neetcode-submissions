class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        #create 2 seperate counts and compare if the counts for each word match
        count1 = defaultdict(int)
        count2 = defaultdict(int)
        for c in s:
            count1[c] += 1
        
        for c in t:
            count2[c] += 1
        
        return count1 == count2



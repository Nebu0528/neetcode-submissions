class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        #apple
        #a3e

        w = 0
        a = 0

        while (w < len(word) and a < len(abbr)):
            if word[w] == abbr[a]:
                w += 1
                a += 1
                continue
            
            if abbr[a] == '0':
                return False
            
            if not (abbr[a].isdigit()) and word[w] != abbr[a]:
                return False
            
            skip = 0
            while a < len(abbr) and abbr[a].isdigit():
                skip = skip * 10 + (int(abbr[a])-0)
                a += 1
            w += skip
        
        return a == len(abbr) and w == len(word)
        
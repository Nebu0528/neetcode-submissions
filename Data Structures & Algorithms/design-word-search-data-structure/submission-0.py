class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            #create a node for it
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endofword = True

    def search(self, word: str) -> bool:
        #use a dfs helper funciton that keep tracks of the node and word index
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    #standard lookup
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.endofword
        return dfs(0, self.root)

        

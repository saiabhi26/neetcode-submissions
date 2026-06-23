class TrieNode:
    def __init__(self):
        self.children = {}
        self.isword = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isword = True

    def search(self, word: str) -> bool:
        def traverse(i, root):
            for j in range(i,len(word)):
                if word[j] == '.':
                    for v in root.children.values():
                        if traverse(j+1,v):
                            return True
                    return False
                else:
                    if word[j] not in root.children:
                        return False
                    root = root.children[word[j]]
            return root.isword
        cur = self.root
        return traverse(0,cur)
class WordDictionary:

    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word: str) -> None:
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = WordDictionary()
            node = node.children[c]
        node.isWord = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            for i in range(index,len(word)):
                if word[i] == '.':
                    for child in node.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if word[i] not in node.children:
                        return False
                    node = node.children[word[i]]
            return node.isWord
        
        return dfs(0,self)

        




class WordDictionary:

    def __init__(self):
        self.children = {}
        self.wordend = False

    def addWord(self, word: str) -> None:
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = WordDictionary()
            node = node.children[c]
        node.wordend = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            for i in range(index, len(word)):
                c = word[i]
                if c == '.':
                    # For each child, recursively check if the rest of the word matches
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in node.children:
                        return False
                    node = node.children[c]
            return node.wordend
        
        return dfs(0, self)

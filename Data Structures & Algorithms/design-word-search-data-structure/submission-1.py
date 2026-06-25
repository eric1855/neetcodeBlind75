# class WordDictionary:

#     def __init__(self):
#         self.children = {}
#         self.wordend = False

#     def addWord(self, word: str) -> None:
#         node = self
#         for c in word:
#             if c not in node.children:
#                 node.children[c] = WordDictionary()
#             node = node.children[c]
#         node.wordend = True

#     def search(self, word: str) -> bool:
#         def dfs(index, node):
#             for i in range(index, len(word)):
#                 c = word[i]
#                 if c == '.':
#                     # For each child, recursively check if the rest of the word matches
#                     for child in node.children.values():
#                         if dfs(i + 1, child):
#                             return True
#                     return False
#                 else:
#                     if c not in node.children:
#                         return False
#                     node = node.children[c]
#             return node.wordend
        
#         return dfs(0, self)

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
        # Using iterative DFS with a stack
        # Stack elements: (index, node)
        stack = [(0, self)]
        
        while stack:
            index, node = stack.pop()
            
            # If we've processed the entire word
            if index == len(word):
                if node.wordend:
                    return True
                continue
                
            c = word[index]
            
            if c == '.':
                # For wildcard, add all children to stack with next index
                for child in node.children.values():
                    stack.append((index + 1, child))
            else:
                # For normal character, check if it exists and continue
                if c in node.children:
                    stack.append((index + 1, node.children[c]))
                    
        return False


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = defaultdict(list)
        for word in strs:
            ls = [0]*26
            for char in word:
                ls[ord(char)-ord('a')] += 1
            dct[tuple(ls)].append(word)
        return list(dct.values())
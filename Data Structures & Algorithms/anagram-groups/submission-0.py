class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            dct = defaultdict(list)
            for word in strs:
                count = [0] * 26
                for char in word:
                    count[ord(char) - ord('a')] += 1
                dct[tuple(count)].append(word)
            return list(dct.values())



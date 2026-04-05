class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        i = -1
        final = []

        for word in strs:
            sc = sorted(word)
            sword = "".join(sc)
            if sword not in groups:
                i += 1
                groups[sword] = i
                final.append([word])
            else:
                final[groups[sword]].append(word)
        return final
            
        
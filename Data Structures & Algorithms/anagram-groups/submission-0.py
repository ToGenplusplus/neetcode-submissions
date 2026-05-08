from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
            examples
            input: ["act","pots","tops","cat","stop","hat"]
            result -> [["hat"],["act", "cat"],["stop", "pots", "tops"]]

            validation
                can input list be empty? [1,1000]
                how large can strs be [1,1000]
                how many characters can strs[i] have [0,100]
                what type of characters can strs[i] have -> lowercase enlgish letters

            constraints
                time and space complexity?
                output order?


            anagarams have the same lenghts of chars and same frequency of chars

            we use a map to store key -> list of anagrams
            we can iterate through strs
                use a frequency array of size 26 to count chars in strs[i]
                use this frequency array as map key

                we check if key for str[i] is in map
                if so we add strs[i] to map - anagrams
                if not we add new key in map and add strs[i] to key in map

            return map values
        """

        anagramGroups = defaultdict(list)

        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            key = '#'.join(str(counts))
            anagramGroups[key].append(s)

        return list(anagramGroups.values())
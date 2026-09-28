class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = {}

        for s in strs:
            # calculate canonical key
            frequency = [0] * 26
            for c in s:
                frequency[ord(c) - ord("a")] += 1
           
            key = "#".join(str(frequency))
            
            if key not in grouped_anagrams:
                grouped_anagrams[key] = []
            
            grouped_anagrams[key].append(s)

        return list(grouped_anagrams.values())

            

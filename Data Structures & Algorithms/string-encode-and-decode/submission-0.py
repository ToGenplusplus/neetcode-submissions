class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        result = []
        for s in strs:
            encoded = f"{len(s)}#{s}"
            result.append(encoded)

        return "".join(result)
        """
            approach, 
            iterate through strs
                for each string s, create a encoded representation
                {len(s)#s}, add this to a result list
            return resultlist.join
        """

    def decode(self, s: str) -> List[str]:
        if not s or s == "":
            return []

        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            
            advance = j + 1 + length

            string = s[j+1: advance]
            
            res.append(string)

            i = advance

        return res
            

        
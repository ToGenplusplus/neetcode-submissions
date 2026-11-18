class Solution:

    def encode(self, strs: List[str]) -> str:
        """
            strs = ["Hello","World"]
            Hello -> 5#Hello
            World -> 5#World
            encoded -> 5#Hello5#World

        """
        res = []
        for s in strs:
            e = f"{len(s)}#{s}"
            res.append(e)
        return "".join(res)

    def decode(self, s: str) -> List[str]:

        """
            5#Hello5#World
        
            i = 0, j = 0
            j+=1 while j != #
            j=1
            len(s) = ints[i:j]
            word = s[j: j + len(s) + 1]
            
        """
        res = []

        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j+= 1

            length = int(s[i:j])
            word = s[j+1: j + 1 + length]
            res.append(word)

            i = j + length + 1

        return res
        
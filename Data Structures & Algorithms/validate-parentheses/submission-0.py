class Solution:
    def isValid(self, s: str) -> bool:
        parens = {"}":"{", "]":"[", ")":"("}
        opens = []

        for paren in s:
            # if its an open paren
            if paren not in parens:
                opens.append(paren)
            else: 
            # closed paren, check if opens has at least 1 element
                if not opens:
                    #invalid
                    return False
                lastOpen = opens.pop()
                if lastOpen != parens[paren]:
                    return False
        return len(opens) == 0
        """
            given
                string s
                s contains {[()]}
                len(s) range [1,1000]
                s can be null
            return
                true -> s is valid parentheses
                false -> s is invalid 

            examples
            s = "([{}])"


            constraints?

            reasoning
            using the following example: s = "([{}])"

            (
            ([
            ([{} - matching closed paren, remove open
            ([] - matching closed paren, remove open
            () matching closed paren, remove open
            ""
            if there is more open than closed parens (or vice versa) -invalid
        """
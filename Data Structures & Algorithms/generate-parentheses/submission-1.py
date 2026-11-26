# My solution:

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        res = []

        def generate(path, open_count, close_count):
            if len(path) == 2 * n:
                res.append("".join(list(path)))

            if open_count < n:
                path.append("(")
                generate(path, open_count + 1, close_count)
                path.pop()

            if open_count > close_count:
                path.append(")")
                generate(path, open_count, close_count + 1)
                path.pop()
        
        generate([], 0, 0)
        return res

        """
            n = 2 -> ()(), (()),

            [],0,0
                0 < 2, add open
                (, 1, 0
                    1 < 2, add open
                        (( 2, 0
                            open = 2, add closed
                                ((),2, 1
                                    closed < n, add closed 
                                        (()), 2, 2
                                            len(path) == 2 * n, add (()) to result
                    open > closed, add closed
                    () 1, 1
                        open < n, add open
                        ()(,2,1
                            closed < open, add closed
                            ()(),2,2
                                len(path) == 2 * n, add ()() to result


        """
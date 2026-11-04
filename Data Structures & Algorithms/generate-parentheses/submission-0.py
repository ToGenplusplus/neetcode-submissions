class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = set()

        def backtrack(string, remainder):
            print(f"input:{string}, remainder: {remainder}")
            if remainder == 0 and string not in res:
                res.add(string)

            if remainder > 0:
                for i in range(len(string)):
                    s_split = list(string)

                    s_split.insert(i,"()")
                    new = "".join(s_split)
                    if new not in res:
                        backtrack(new, remainder - 1)



        backtrack("()", n - 1)
        return list(res)
        """
            n = 3

            start, remainder

            (), n - 1 = 2

                ()(), 1
                    ()()(), 0
                        remainder is 0 - add to result
                    (())(),0 - add to result
                    ()()() - duplicate skip
                    ()(()),0 - add to result
                    ()()() - duplicate skip

                (()), 1
                    ()(()) - duplicate skip
                    (()()),0 - add to result
                    ((())),0 - add to result
                    (()()),0 - duplicate skuo
                    (())(),0 - duplicate skip


                ()(),1 - duplicate skip

        """
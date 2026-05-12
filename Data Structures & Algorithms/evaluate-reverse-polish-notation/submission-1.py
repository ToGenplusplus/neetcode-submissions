class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
            given
                array of strings
                array range []
                array[i] range []
            return
               integer representing reverse polish notation result

            examples


            constraints

        """
        operands = []
        operators = set(["+","-","*","/"])

        for token in tokens:
            if token not in operators:
                operands.append(int(token))
            else:
                #get the last two operands
                right,left = operands.pop(), operands.pop()
                if token == "+":
                    operands.append(left + right)
                elif token == "-":
                    operands.append(left - right)
                elif token == "*":
                    operands.append(left * right)
                else:
                    operands.append(int(left / right))
        return operands[0]

        """
            ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
            [10,6,12, -11]
            [10,6,-132] / 
            [10,-22] * 
            [-220,17]+
        """
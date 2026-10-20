class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = {
            "+",
            "*",
            "-",
            "/",
            }
        operands = []

        for token in tokens:
            if token not in operators:
                operands.append(int(token))
            else:
                right, left = operands.pop(), operands.pop()

                if token == "+":
                    operands.append(left + right)
                elif token == "-":
                    operands.append(left - right)
                elif token == "*":
                    operands.append(left * right)
                else:
                    operands.append(int(left / right))

        return operands[0]


from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = deque()
        operators_set = set(['+', '-', '*', '/'])

        for token in tokens:
            if token in operators_set:
                num2 = num_stack.pop()
                num1 = num_stack.pop()

                if token == '+':
                    num_stack.append(num1 + num2)
                elif token == '-':
                    num_stack.append(num1 - num2)
                elif token == '*':
                    num_stack.append(num1 * num2)
                else:
                    num_stack.append(int(num1 / num2))
            else:
                num_stack.append(int(token))

        return num_stack[0]

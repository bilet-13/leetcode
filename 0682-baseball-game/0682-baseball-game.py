class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                if len(stack) >= 2:
                    prev_sum = stack[-1] + stack[-2]
                    stack.append(prev_sum)

            elif op == "D":
                double_num = 2 * stack[-1]
                stack.append(double_num)
                
            elif op == "C":
                if stack:
                    stack.pop()
            else:
                try:
                    new_score = int(op)
                    stack.append(new_score)
                except:
                    pass

        return sum(stack)
        
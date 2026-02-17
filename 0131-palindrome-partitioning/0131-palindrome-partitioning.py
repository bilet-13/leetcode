class Solution:
    def partition(self, s: str) -> List[List[str]]:
          # backtrcking -> how to transfer it into a search tree problem
        # define the cur char is the node we want to add it to existed or create a new one
        # leaf node: the len of cur == len(s)
        # 
        result = []

        def backtrack(start_index, current_path):
            if start_index == len(s):
                result.append(current_path[:])
                return

            for end_idx in range(start_index + 1, len(s) + 1):
                substr = s[start_index: end_idx]

                if substr == substr[::-1]:

                    current_path.append(substr)

                    backtrack(end_idx, current_path)

                    current_path.pop()

        backtrack(0, [])
        return result
        
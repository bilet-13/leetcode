class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # so the town judge would be the  condition: node that indegree is n - 1  and out degree is 0 
        # the edge is define ai -> bi when trust[i] = [ai, bi]
        # so just check if there is only one node satify the condiiton
        # time complexity o(n + len(trust)) at most o(n ^ 2)
        in_degrees = [0 for _ in range(n + 1)]
        out_degrees = [0 for _ in range(n + 1)]

        for a, b in trust:
            in_degrees[b] += 1
            out_degrees[a] += 1

        town_judge = -1

        for i in range(1, n + 1):
            if in_degrees[i] == n - 1 and out_degrees[i] == 0:
                if town_judge != -1:
                    return -1 # multiple answer

                town_judge = i

        return town_judge
        
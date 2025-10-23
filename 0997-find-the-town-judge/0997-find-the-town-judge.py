class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_degrees = [0 for _ in range(n + 1)]
        out_degrees = [0 for _ in range(n + 1)]

        for person_a, person_b in trust:
            in_degrees[person_b] += 1
            out_degrees[person_a] += 1
        
        people_everybody_trust = []

        for i in range(1, n + 1):
            if in_degrees[i] == n - 1:
                people_everybody_trust.append(i)
        
        if len(people_everybody_trust) != 1:
            return -1
        
        return people_everybody_trust[0] if out_degrees[people_everybody_trust[0]] == 0 else -1 
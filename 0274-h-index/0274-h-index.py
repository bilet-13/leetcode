class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort(reverse=True)

        for i in range(len(citations)):
            num_papers = i+1
            if num_papers == citations[i]:
                return num_papers
            elif num_papers > citations[i]:
                return num_papers - 1
        return len(citations)
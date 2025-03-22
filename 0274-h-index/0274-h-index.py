class Solution:
    def hIndex(self, citations: List[int]) -> int:
        non_increased_citations = sorted(citations, reverse=True)

        h_index = 0

        for index in range(len(non_increased_citations)):
            if non_increased_citations[index] >= index + 1:
                h_index = index + 1
            else:
                return h_index

        return h_index

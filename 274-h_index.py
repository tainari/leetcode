"""
https://leetcode.com/problems/h-index/
Beats: 100%
Difficulty: Medium
"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        # H-index: N papers with >= N citations
        # count_citations[N] = number of papers with N citations
        count_citations = [0] * (max(citations) + 1)
        for citation in citations:
            count_citations[citation] += 1
        print(count_citations)
        # find the cumulative number
        # i.e., cumulative_citations[N] = number of papers with at least N citations
        cumulative_citations = [0] * len(count_citations)
        for ind in range(len(count_citations) - 1, -1, -1):
            if ind < len(cumulative_citations) - 1:
                cumulative_citations[ind] = cumulative_citations[ind+1] + count_citations[ind]
            else:
                cumulative_citations[ind] = count_citations[ind]
            if cumulative_citations[ind] >= ind:
                return ind
        return len(citations)